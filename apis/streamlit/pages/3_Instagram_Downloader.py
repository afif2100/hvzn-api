from PIL import Image
from io import BytesIO
from stqdm import stqdm
from instaloader import Post

import instaloader
import pandas as pd
import requests
import streamlit as st


USER = "ahvzn21"


def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


def text_field(label, columns=None, **input_params):
    c1, c2 = st.columns(columns or [1, 4])

    # Display field name with some alignment
    c1.markdown("##")
    c1.markdown(label)

    # Sets a default key parameter to avoid duplicate key errors
    input_params.setdefault("key", label)

    # Forward text input parameters
    return c2.text_input("", **input_params)


@st.cache
def convert_df(df):
    return df.to_csv().encode("utf-8")


def st_download_df(csv_name):
    # download button
    csv = convert_df(df)

    st.download_button(
        "Press to Download",
        csv,
        csv_name,
        "text/csv",
        key="download-csv",
    )


# Start
st.title("Instagram Downloader")

# Get instance
def login_instagram(USER):
    L = instaloader.Instaloader()
    L.load_session_from_file(USER)
    st.success(f"Login Success")
    return L


# get url from input
POST_URL_DEFAULT = "https://www.instagram.com/p/CgJ0WZNggfB/"
url_post = text_field("Post Url", value= POST_URL_DEFAULT)
_get_comment = st.checkbox("Get Comment")

if st.button("Get Post"):
    # instagram login
    L = login_instagram(USER)

    SHORTCODE = url_post.split("/")[-1]
    if len(SHORTCODE) < 3:
        SHORTCODE = url_post.split("/")[-2]

    # get post
    post = Post.from_shortcode(L.context, SHORTCODE)
    st.write(
        f"Get Post from username : https://www.instagram.com/{post.owner_username}/"
    )

    _pcl = post.comments
    if _get_comment and (_pcl > 0):
        # get comment
        comment_list = []
        for com_ in stqdm(post.get_comments()):
            comment_list.append(com_._asdict())

        with st.expander(f"Comment Count: {_pcl}"):
            # parse comment
            df = pd.DataFrame(comment_list)
            df["owner"] = df["owner"].apply(lambda x: x.username)
            df = df[["id", "created_at_utc", "text", "owner", "likes_count"]]
            st.write(df)

            st_download_df(f"instagram_comment_{post.owner_username}_{SHORTCODE}.csv",)


    if post.mediacount == 1:
        with st.expander(f"See images"):
            img = load_image(post.url)
            st.image(img)
    else:
        for i, sidecar in enumerate(post.get_sidecar_nodes()):
            # TO-DO: Enable Video Streaming
            if not sidecar.is_video:
                with st.expander(f"See images {i}"):
                    img = load_image(sidecar.display_url)
                    st.image(img)

            else:
                with st.expander(f"See Videos {i}"):
                    resp_ = requests.get(sidecar.video_url)
                    content_ = BytesIO(resp_.content)
                    st.video(content_)

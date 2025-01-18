from instagrapi import Client
import time
import random
import logging


logging.basicConfig(filename='unfollow.log', level=logging.INFO, format='%(asctime)s - %(message)s')

DAILY_UNFOLLOW_LIMIT = 50
MIN_DELAY = 60
MAX_DELAY = 120

#
def login(username, password):
    cl = Client()
    try:
        cl.login(username, password)
        logging.info("Logged in successfully.")
        return cl
    except Exception as e:
        logging.error(f"Login failed: {e}")
        raise


def get_non_followers(cl):
    try:

        followers = set(cl.user_followers(cl.user_id).keys())

        following = set(cl.user_following(cl.user_id).keys())

        non_followers = following - followers
        logging.info(f"Found {len(non_followers)} non-followers.")
        return list(non_followers)
    except Exception as e:
        logging.error(f"Error fetching non-followers: {e}")
        raise


def unfollow_non_followers(cl, non_followers):
    unfollowed_count = 0
    for user_id in non_followers:
        if unfollowed_count >= DAILY_UNFOLLOW_LIMIT:
            logging.info("Daily unfollow limit reached. Stopping.")
            break

        try:
            cl.user_unfollow(user_id)
            unfollowed_count += 1
            logging.info(f"Unfollowed user: {user_id} | Total unfollowed: {unfollowed_count}")
        except Exception as e:
            logging.error(f"Error unfollowing {user_id}: {e}")


        delay = random.randint(MIN_DELAY, MAX_DELAY)
        logging.info(f"Waiting for {delay} seconds before next action.")
        time.sleep(delay)

    logging.info("Unfollow process completed.")


def main():
    username = "YOUR_USERNAME"
    password = "YOUR_PASSWORD"

    try:
        cl = login(username, password)
        non_followers = get_non_followers(cl)
        unfollow_non_followers(cl, non_followers)
    except Exception as e:
        logging.error(f"Script failed: {e}")

if __name__ == "__main__":
    main()
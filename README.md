# InstaUnfollower
A Python script to unfollow users who don't follow you back on Instagram using the `instagrapi` library. This script is designed to mimic human behavior to avoid triggering Instagram's anti-spam mechanisms.

---

## Features
- **Gradual Unfollowing**: Unfollows users slowly to avoid detection.
- **Daily Limit**: Stops after unfollowing a set number of accounts per day.
- **Logging**: Logs all actions and errors to a file for review.
- **Customizable**: Adjust the unfollow limit and delays to suit your needs.

---

## Prerequisites
- Python 3.7 or higher
- Instagram account credentials
- Basic knowledge of Python and Git

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/HITMAN949/InstaUnfollower.git
   cd InstaUnfollower
2. **Create Virtual Environement**:
For windows:
```bash
python -m venv .venv

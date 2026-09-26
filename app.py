"""
Snack Attack! - Flask Web Application Runner
Re-exports the Flask app from api.index for local development and test execution.
"""
from api.index import (
    app,
    handler,
    application,
    load_high_score,
    save_high_score,
    load_leaderboard,
    add_leaderboard_entry,
    SNACK_METADATA
)

if __name__ == "__main__":
    print("==================================================")
    print(">>> Snack Attack! Flask Web Server Starting...")
    print(">>> Open your browser at: http://127.0.0.1:5000")
    print("==================================================")
    app.run(host="0.0.0.0", port=5000, debug=False)

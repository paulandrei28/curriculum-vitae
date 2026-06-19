import os
from flask import Flask, render_template, send_from_directory, request, jsonify
from curriculum_vitae_content import curriculum_vitae_content

app = Flask(__name__)


@app.route("/")
def curriculum_vitae_homepage():
    return render_template(
        "curriculum_vitae_homepage.html", curriculum_vitae=curriculum_vitae_content
    )


@app.route("/download/curriculum-vitae")
def download_curriculum_vitae():
    return send_from_directory(
        "static/documents",
        "Paul_Sipos_CV.pdf",
        as_attachment=True,
        download_name="Paul_Sipos_Curriculum_Vitae.pdf",
    )


@app.route("/track-game-event", methods=["POST"])
def track_game_event():
    """Endpoint to receive game event tracking data."""
    try:
        data = request.get_json()
        # Optional: Log to backend for additional analytics
        app.logger.info(f"Game Event: {data.get('event')} - {data.get('data')}")
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        app.logger.error(f"Error tracking game event: {e}")
        return jsonify({"status": "error"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

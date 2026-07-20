"""
Banalyzer Streamlit Application.

Presentation layer for the Banana Ripeness Predictor.
"""

from __future__ import annotations

import streamlit as st
from PIL import Image

from config import (
    CLASS_NAMES,
    MODEL,
    PROJECT,
)

from predict import (
    load_model,
    predict_image,
    PredictionResult,
)

from config import PREDICTION_COLORS
from dataclasses import dataclass

import logging
import tempfile
import time
from pathlib import Path

from utils.logger import get_logger

logger = get_logger(__name__)


#1 UI Metadata
# CLASS_METADATA
# PREDICTION_INSIGHTS

CLASS_METADATA = {
    "Unripe": {
        "icon": "🟢",
        "title": "Unripe",
        "badge": "Early Stage",
        "description": "...",
        "color": "green",
        "order": 0,
    },
    "Ripe": {
        "icon": "🟡",
        "title": "Ripe",
        "badge": "Ready to Eat",
        "description": "...",
        "color": "yellow",
        "order": 1,
    },
    "Overripe": {
        "icon": "🟤",
        "title": "Overripe",
        "badge": "Use Soon",
        "description": "...",
        "color": "orange",
        "order": 2,
    },
    "Rotten": {
        "icon": "⚫",
        "title": "Rotten",
        "badge": "Discard",
        "description": "...",
        "color": "red",
        "order": 3,
    },
}

MODEL_METADATA = {
    "architecture": {
        "title": "Architecture",
        "icon": "🧠",
        "value": "MobileNetV2",
        "color": "#2563EB",
    },
    "accuracy": {
        "title": "Test Accuracy",
        "icon": "🎯",
        "value": "72.5%",
        "color": "#22C55E",
    },
    "framework": {
        "title": "Framework",
        "icon": "⚙️",
        "value": "TensorFlow 2.20",
        "color": "#8B5CF6",
    },
    "input_size": {
        "title": "Input Resolution",
        "icon": "🖼️",
        "value": "224 × 224",
        "color": "#F59E0B",
    },
    "classes": {
        "title": "Output Classes",
        "icon": "🍌",
        "value": "4",
        "color": "#FACC15",
    },
    "device": {
        "title": "Inference Device",
        "icon": "💻",
        "value": "CPU",
        "color": "#06B6D4",
    },
}

PREDICTION_INSIGHTS = {
    "Unripe": {
        "status": "Not Ready for Consumption",
        "best_use": "Allow the banana to ripen naturally before eating.",
        "recommendation": (
            "Store at room temperature for 2–5 days. "
            "Avoid refrigeration to promote even ripening."
        ),
    },
    "Ripe": {
        "status": "Ready to Eat",
        "best_use": "Ideal for fresh consumption, smoothies, and fruit salads.",
        "recommendation": (
            "Consume within the next 2–3 days for the best flavor and texture."
        ),
    },
    "Overripe": {
        "status": "Overripe",
        "best_use": "Excellent for baking, banana bread, pancakes, and desserts.",
        "recommendation": (
            "Use soon or refrigerate to slow further ripening."
        ),
    },
    "Rotten": {
        "status": "Not Safe for Consumption",
        "best_use": "Not recommended for consumption.",
        "recommendation": (
            "Discard the fruit to avoid potential food safety risks."
        ),
    },
}


#2 Core UI Configuration
#configure_page ()
#load_css ()
#get_model ()

def configure_page() -> None:
    """Configure the Streamlit page."""

    st.set_page_config(
        page_title=PROJECT.name,
        page_icon="🍌",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def load_css() -> None:
    """Load the application's custom CSS."""

    css_path = Path("assets") / "styles.css"

    if not css_path.exists():
        return

    with css_path.open("r", encoding="utf-8") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True,
        )


@st.cache_resource
def get_model() -> keras.Model:
    """
    Load and cache the trained TensorFlow model.

    Returns
    -------
    keras.Model
        Loaded TensorFlow model.
    """
    return load_model()

@dataclass(frozen=True)
class ConfidenceMetadata:
    """Presentation metadata for the confidence badge."""

    label: str
    color: str
    icon: str


#3 Input & Inference
# render_uploader ()
# run_prediction ()

def render_uploader():
    """
    Render the image uploader.

    Returns
    -------
    UploadedFile | None
        Uploaded image file.
    """

    uploaded_file = st.file_uploader(
        "Upload a Banana Image",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_file is None:
        return None

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True,
    )

    return uploaded_file

def run_prediction(
    uploaded_file,
) -> PredictionResult | None:
    """
    Run banana ripeness prediction.

    Parameters
    ----------
    uploaded_file
        Uploaded image.

    Returns
    -------
    PredictionResult | None
    """

    if uploaded_file is None:
        return None

    model = get_model()

    with tempfile.NamedTemporaryFile(
        suffix=Path(uploaded_file.name).suffix,
        delete=False,
    ) as temp_file:

        temp_file.write(uploaded_file.getbuffer())

        temp_path = Path(temp_file.name)

    try:
        start_time = time.perf_counter()

        prediction = predict_image(
            model=model,
            image_path=temp_path,
        )

        inference_time_ms = (
            time.perf_counter() - start_time
        ) * 1000

        result = PredictionResult(
            predicted_class=prediction.predicted_class,
            confidence=prediction.confidence,
            probabilities=prediction.probabilities,
            inference_time_ms=inference_time_ms,
        )

        logger.info(
            "Prediction completed successfully in %.2f ms.",
            inference_time_ms,
        )

        return result

    except Exception:
        logger.exception(
            "Prediction failed."
        )

        st.error(
            (
                "Unable to analyze the uploaded image.\n\n"
                "Please upload a clear JPG, JPEG, or PNG image "
                "containing a single banana."
            )
        )

        return None

    finally:
        temp_path.unlink(missing_ok=True)


#4 Reusable UI Components
#render_card ()
#get_confidence_metadata ()

def render_card(
    *,
    title: str,
    value: str,
    color: str = "#111827",
    icon: str = "",
) -> None:
    """
    Render a reusable dashboard card.
    """

    with st.container(border=True):

        st.caption(title)

        st.markdown(
            f"""
<h2 style="
    color:{color};
    text-align:center;
    margin:0;
    padding:12px 0;
">
    {icon} {value}
</h2>
""",
            unsafe_allow_html=True,
        )


def get_confidence_metadata(
    confidence: float,
) -> tuple[str, str, str]:
    """
    Return the confidence badge metadata.

    Parameters
    ----------
    confidence : float
        Prediction confidence score.

    Returns
    -------
    tuple[str, str, str]
        Badge label, color, and icon.
    """

    if confidence >= 0.80:
        return (
            "High Confidence",
            "#16A34A",   # Green
            "🟢",
        )

    if confidence >= 0.60:
        return (
            "Medium Confidence",
            "#F59E0B",   # Amber
            "🟡",
        )

    return (
        "Low Confidence",
        "#DC2626",       # Red
        "🔴",
    )


#5 Prediction Components -

#render_prediction_summary ()

#render_probability_section ()

#render_prediction_explanation ()

#get_confidence_interpretation () (Prediction Explanation)
#get_runner_up_prediction () (Prediction Explanation)

#render_prediction_insights ()

#render_model_information () (or)
#render_prediction_metadata ()

#render_banana_lifecycle ()

#render_model_performance ()

#render_prediction ()

def render_prediction_summary(
    result: PredictionResult,
) -> None:
    """
    Render the prediction and confidence summary cards.
    """

    prediction_color = PREDICTION_COLORS[result.predicted_class]

    (
        confidence_label,
        confidence_color,
        confidence_icon,
    ) = get_confidence_metadata(
        result.confidence,
    )

    prediction_col, confidence_col = st.columns(2)

    with prediction_col:
        render_card(
            title="Prediction",
            value=result.predicted_class,
            color=prediction_color,
            icon="🍌",
        )

    with confidence_col:
        render_card(
            title=confidence_label,
            value=f"{result.confidence:.2%}",
            color=confidence_color,
            icon=confidence_icon,
        )


def render_confidence_gauge(
    result: PredictionResult,
) -> None:
    """
    Render a visual confidence gauge for the current prediction.
    """

    st.subheader("📈 Confidence Gauge")

    level, description = get_confidence_interpretation(
        result.confidence
    )

    badge_label, badge_color, badge_icon = (
        get_confidence_metadata(result.confidence)
    )   

    render_card(
        title="Confidence",
        value=f"{result.confidence:.2%}",
        icon=badge_icon,
        color=badge_color,
    )

    st.progress(result.confidence)

    st.caption("Low ◀──────────────▶ High")

    st.caption(badge_label)

    st.info(
        f"**Confidence Level:** {level}\n\n{description}"
    )


def render_probability_section(
    result: PredictionResult,
) -> None:
    """
    Render class probabilities.
    """

    st.divider()

    st.subheader("Probability Distribution")

    for class_name, probability in result.probabilities.items():

        label_col, value_col = st.columns([4, 1])

        meta = CLASS_METADATA.get(class_name, {})
        emoji = meta.get("emoji", "🍌")

        st.write(f"{emoji} **{class_name}**")

        st.progress(
            float(probability),
            text=f"{probability:.1%}"
        )


def render_prediction_explanation(
    result: PredictionResult,
) -> None:
    """
    Render a human-readable explanation of the prediction.
    """

    st.subheader("🧠 Prediction Explanation")

    confidence_level, explanation = (
        get_confidence_interpretation(result.confidence)
    )

    runner_up_class, runner_up_probability = (
        get_runner_up_prediction(result)
    )

    left_col, right_col = st.columns(2)

    with left_col:
        render_card(
            title="Confidence Level",
            value=confidence_level,
            icon="📈",
            color="#22C55E",
        )

    with right_col:
        render_card(
            title="Runner-up Prediction",
            value=f"{runner_up_class} ({runner_up_probability:.2%})",
            icon=CLASS_METADATA[runner_up_class]["icon"],
            color="#F59E0B",
        )

    st.info(
        (
            f"The model predicts **{result.predicted_class}** "
            f"with **{result.confidence:.2%}** confidence.\n\n"
            f"The second most likely class is "
            f"**{runner_up_class}** "
            f"with **{runner_up_probability:.2%}** probability.\n\n"
            f"**Interpretation:** {explanation}"
        )
    )


def get_confidence_interpretation(
    confidence: float,
) -> tuple[str, str]:
    """
    Return a human-readable confidence level and explanation.
    """

    if confidence >= 0.90:
        return (
            "Very High",
            "The model is highly confident in this prediction.",
        )

    if confidence >= 0.75:
        return (
            "High",
            "The prediction is reliable with minimal ambiguity.",
        )

    if confidence >= 0.60:
        return (
            "Moderate",
            (
                "The prediction is reasonably confident, "
                "but another ripeness stage also received a "
                "meaningful probability."
            ),
        )

    return (
        "Low",
        (
            "The model is uncertain. Consider capturing "
            "another image with better lighting and focus."
        ),
    )


def get_runner_up_prediction(
    result: PredictionResult,
) -> tuple[str, float]:
    """
    Return the second most probable prediction.
    """

    ranked_predictions = sorted(
        result.probabilities.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return ranked_predictions[1]


def render_prediction_insights(
    result: PredictionResult,
) -> None:
    """
    Render prediction insights based on the predicted class.
    """

    insights = PREDICTION_INSIGHTS.get(
        result.predicted_class,
    )

    if insights is None:
        return

    st.divider()

    st.subheader("💡 Ripeness Insights")

    with st.container(border=True):

        st.markdown("#### 🍌 Ripeness Status")
        st.write(insights["status"])

        st.divider()

        st.markdown("#### 🍽️ Recommended Use")
        st.write(insights["best_use"])

        st.divider()

        st.markdown("#### 💡 Recommendation")
        st.write(insights["recommendation"])    


def render_prediction_metadata(
    result: PredictionResult,
) -> None:
    """
    Render prediction metadata cards.
    """

    st.divider()

    st.subheader("📊 Prediction Metadata")

    top_left, top_right = st.columns(2)

    with top_left:
        render_card(
            title="Architecture",
            value=PROJECT.model_name,
            color="#2563EB",
            icon="🧠",
        )

    with top_right:
        render_card(
            title="Top Prediction",
            value=f"{result.confidence:.2%}",
            color="#16A34A",
            icon="🎯",
        )

    bottom_left, bottom_right = st.columns(2)

    with bottom_left:
        render_card(
            title="Input Resolution",
            value=f"{MODEL.image_size} × {MODEL.image_size}",
            color="#F59E0B",
            icon="🖼️",
        )

    with bottom_right:
        render_card(
            title="Prediction Time",
            value=f"{round(result.inference_time_ms)} ms",
            color="#8B5CF6",
            icon="⚡",
        )


def render_banana_lifecycle(
    result: PredictionResult,
) -> None:
    """
    Render a horizontal banana ripeness lifecycle visualization.

    Args:
        result: Prediction result returned by the inference layer.
    """
    st.subheader("🍌 Banana Lifecycle")

    stages = sorted(
        CLASS_METADATA.items(),
        key=lambda item: item[1]["order"],
    )

    current_order = CLASS_METADATA[result.predicted_class]["order"]

    layout = [1]
    for _ in range(len(stages) - 1):
        layout.extend([0.25, 1])

    cols = st.columns(layout)

    col_index = 0

    for index, (stage_name, metadata) in enumerate(stages):
        stage_order = metadata["order"]

        if stage_order < current_order:
            status_icon = "✅"
            status_text = "Completed"

        elif stage_order == current_order:
            status_icon = "🟢"
            status_text = "Current"

        else:
            status_icon = "⚪"
            status_text = "Upcoming"

        with cols[col_index]:
            st.markdown(
                f"""
<div style="text-align:center">

<h1>{metadata["icon"]}</h1>

<b>{stage_name}</b>

<br>

{status_icon} {status_text}

</div>
""",
                unsafe_allow_html=True,
            )

        col_index += 1

        if index < len(stages) - 1:
            with cols[col_index]:
                st.markdown(
                    """
<div style="text-align:center;
font-size:34px;
padding-top:55px;">
➡️
</div>
""",
                    unsafe_allow_html=True,
                )

            col_index += 1


def render_model_performance() -> None:
    """
    Render the model performance dashboard.
    """
    st.divider()
    st.subheader("📊 Model Performance")

    metrics = list(MODEL_METADATA.values())

    columns = st.columns(3)

    for index, metric in enumerate(metrics):
        with columns[index % 3]:
            render_card(
                title=metric["title"],
                value=metric["value"],
                icon=metric["icon"],
                color=metric["color"],
            )


def render_prediction(result: PredictionResult) -> None:
    """Render the complete prediction dashboard."""

    render_prediction_analysis(result)

    render_prediction_details(result)


# Dashboard Sections
#Section 1
def render_prediction_analysis(
    result: PredictionResult,
) -> None:
    """
    Render analysis related to the prediction.
    """

    render_prediction_summary(result)

    render_confidence_gauge(result)

    render_probability_section(result)

    render_prediction_explanation(result)

    render_prediction_insights(result)

#Section 2
def render_prediction_details(
    result: PredictionResult,
) -> None:
    """
    Render supplementary prediction details.
    """

    render_prediction_metadata(result)

    render_banana_lifecycle(result)

    render_model_performance()


#6 Layout Components

#render_sidebar ()

#render_header ()

#render_footer ()

def render_sidebar() -> None:
    """Render the application sidebar."""

    with st.sidebar:
        st.title(f"🍌 {PROJECT.name}")
        st.caption(PROJECT.description)

        st.divider()

        st.subheader("Model")

        st.write(f"**Architecture:** {PROJECT.model_name}")
        st.write(f"**Version:** {PROJECT.version}")

        st.metric(
            label="Test Accuracy",
            value=f"{PROJECT.model_accuracy:.1f}%",
        )

        st.divider()

        st.subheader("Classes")

        for class_name in CLASS_NAMES:
            st.write(f"• {class_name}")

        st.divider()

        st.subheader("Input")

        st.write(
            f"Image Size: {MODEL.image_size} × {MODEL.image_size}"
        )


def render_header() -> None:
    """Render the application header."""

    st.title("🍌 Banalyzer")

    st.markdown(
        """
        Predict the ripeness stage of a banana using a
        **MobileNetV2 Transfer Learning** model.
        """
    )

    st.divider()


def render_footer() -> None:
    """Render the application footer."""

    st.divider()

    st.caption(
        f"{PROJECT.name} v{PROJECT.version} | "
        "Built with TensorFlow & Streamlit"
    )


#7 Application Entry Point

#main ()

def main() -> None:
    """Application entry point."""

    configure_page()

    load_css()
    # Warm up the cached model during application startup.
    get_model()

    render_sidebar()

    render_header()

    left_col, right_col = st.columns(
        [1.2, 1],
        gap="large",
    )

    with left_col:
        with st.container(border=True):

            st.subheader("📷 Uploaded Image")

            uploaded_file = render_uploader()

    result: PredictionResult | None = None

    with right_col:
        with st.container(border=True):

            st.subheader("🍌 Prediction")

            if uploaded_file:

                predict_clicked = st.button(
                    "🔍 Predict Ripeness",
                    use_container_width=True,
                )

                if predict_clicked:
                    logger.info(
                        "Prediction requested for '%s'.",
                        uploaded_file.name,
                    )
                    result = run_prediction(uploaded_file)

            if result is not None:
                render_prediction(result)

    render_footer()


if __name__ == "__main__":
    main()

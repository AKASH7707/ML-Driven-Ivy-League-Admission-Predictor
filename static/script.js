window.onload = function() {
    // Check if there's a prediction_text and scroll to the prediction div
    const predictionText = "{{ prediction_text }}";
    if (predictionText) {
        document.querySelector('.prediction').scrollIntoView({ behavior: 'smooth' });
    }
};
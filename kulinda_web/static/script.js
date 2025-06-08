document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("upload-form");
  if (!form) return; // Prevent execution on other pages

  const input = document.getElementById("image-input");
  const resultWrapper = document.getElementById("result-wrapper");
  const errorBox = document.getElementById("error");
  const imagePreview = document.getElementById("uploaded-image");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    resultWrapper.style.display = "none";
    errorBox.style.display = "none";

    const file = input.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onloadend = async () => {
      const base64 = reader.result;

      // Show image preview
      imagePreview.src = base64;
      imagePreview.style.display = "block";

      try {
        const response = await fetch("/predict", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ image: base64 }),
        });

        const data = await response.json();
        if (response.ok) {
          document.getElementById("label").textContent = data.label;
          document.getElementById("confidence").textContent = data.confidence;
          document.getElementById("time").textContent = data.time;
          resultWrapper.style.display = "flex"; // Show result + image side-by-side
        } else {
          errorBox.textContent = data.error || "Something went wrong.";
          errorBox.style.display = "block";
        }
      } catch (err) {
        errorBox.textContent = "Error: " + err.message;
        errorBox.style.display = "block";
      }
    };

    reader.readAsDataURL(file);
  });
});

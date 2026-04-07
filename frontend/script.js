// ============================================================
// script.js
// Handles the "Run Prediction" button click:
// 1. Reads input values
// 2. Sends POST request to FastAPI backend
// 3. Displays the result
// ============================================================

// The URL of our FastAPI backend
const API_URL = "http://44.222.125.196:8000/predict";


// ---- Main predict function ----
// Called when the user clicks the "Run Prediction" button
async function predict() {

  // --- Step 1: Read the values from the input fields ---
  const age         = document.getElementById("age").value.trim();
  const balance     = document.getElementById("balance").value.trim();
  const creditScore = document.getElementById("creditScore").value.trim();

  // --- Step 2: Validate inputs (make sure they're not empty) ---
  if (!age || !balance || !creditScore) {
    showError("Please fill in all three fields before predicting.");
    return;
  }

  if (isNaN(age) || isNaN(balance) || isNaN(creditScore)) {
    showError("All fields must be valid numbers.");
    return;
  }

  // --- Step 3: Show loading spinner and disable the button ---
  showLoading(true);
  hideResult();

  try {
    // --- Step 4: Send POST request to the backend ---
    // fetch() is the browser's built-in way to call APIs
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"  // Tell the server we're sending JSON
      },
      body: JSON.stringify({
        age: parseFloat(age),
        balance: parseFloat(balance),
        credit_score: parseFloat(creditScore)
        // Note: 'credit_score' must match the Pydantic field name in app.py
      })
    });

    // --- Step 5: Parse the JSON response ---
    const data = await response.json();

    if (!response.ok) {
      // If the server returned an error (e.g., 500), show the detail message
      showError(data.detail || "Server error. Please try again.");
      return;
    }

    // --- Step 6: Display the prediction result ---
    showResult(data.prediction);

  } catch (error) {
    // This catches network errors (e.g., backend not running)
    showError(
      "Cannot connect to the API.\n" +
      "Make sure the backend is running at http://localhost:8000"
    );
    console.error("Fetch error:", error);

  } finally {
    // Always hide the loading spinner when done (success or error)
    showLoading(false);
  }
}

// ---- Helper: Show / hide loading spinner ----
function showLoading(isLoading) {
  const btn     = document.getElementById("predictBtn");
  const loading = document.getElementById("loading");

  if (isLoading) {
    btn.disabled = true;
    loading.classList.add("visible");
  } else {
    btn.disabled = false;
    loading.classList.remove("visible");
  }
}

// ---- Helper: Show prediction result ----
function showResult(prediction) {
  const box      = document.getElementById("resultBox");
  const text     = document.getElementById("resultText");
  const meta     = document.getElementById("resultMeta");

  // Clear previous state classes
  box.classList.remove("success", "danger", "error");

  text.textContent = prediction;
  meta.textContent = `Predicted at ${new Date().toLocaleTimeString()}`;

  // Color green if "Will Not Churn", red if "Will Churn"
  if (prediction.includes("Will Not")) {
    box.classList.add("success");
  } else {
    box.classList.add("danger");
  }

  box.classList.add("visible");
}

// ---- Helper: Show error in result box ----
function showError(message) {
  const box  = document.getElementById("resultBox");
  const text = document.getElementById("resultText");
  const meta = document.getElementById("resultMeta");

  box.classList.remove("success", "danger");
  box.classList.add("visible", "error");
  text.textContent = "⚠ " + message;
  meta.textContent = "";
}

// ---- Helper: Hide result box ----
function hideResult() {
  const box = document.getElementById("resultBox");
  box.classList.remove("visible", "success", "danger", "error");
}

// ---- Allow pressing Enter key to trigger prediction ----
document.addEventListener("keydown", function (e) {
  if (e.key === "Enter") {
    predict();
  }
});

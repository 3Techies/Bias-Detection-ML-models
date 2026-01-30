# =========================
# Dataset Configuration
# =========================

DATASET_NAME = "Loan Approval Dataset"
DATA_PATH = "data/loan_data.csv"


# =========================
# Prediction Task
# =========================

# Column the model should predict
TARGET_COLUMN = "loan_approved"

# Value considered as a positive outcome
POSITIVE_LABEL = 1   # or "Yes", depending on dataset


# =========================
# Fairness Configuration
# =========================

# Sensitive attribute to check bias on
SENSITIVE_ATTRIBUTE = "person_gender"

# Define groups explicitly
PRIVILEGED_GROUP = "male"
UNPRIVILEGED_GROUP = "female"


# =========================
# Train / Test Split
# =========================

TEST_SIZE = 0.2
RANDOM_STATE = 42


# =========================
# Models to Use (Week 2+)
# =========================

MODELS = [
    "logistic_regression",
    "random_forest"
]

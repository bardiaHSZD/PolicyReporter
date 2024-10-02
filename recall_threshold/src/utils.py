# src/utils.py

def calculate_metrics(TP, FP, TN, FN):
    """
    Calculate precision, recall, F1 score, false positive rate (FPR), and specificity (TNR).
    
    Args:
        TP (int): True Positives
        FP (int): False Positives
        TN (int): True Negatives
        FN (int): False Negatives
    
    Returns:
        tuple: Precision, recall, F1 score, FPR, and TNR.
    """
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    fpr = FP / (FP + TN) if (FP + TN) > 0 else 0  # False Positive Rate
    tnr = TN / (TN + FP) if (TN + FP) > 0 else 0  # True Negative Rate (Specificity)
    return precision, recall, f1, fpr, tnr


def calculate_composite_score(precision, recall, f1, fpr, weights):
    """
    Calculate a composite score based on weighted metrics.
    
    Args:
        precision (float): Precision value
        recall (float): Recall value
        f1 (float): F1 score
        fpr (float): False Positive Rate
        weights (dict): Weights for the metrics
    
    Returns:
        float: The composite score.
    """
    return (weights['precision'] * precision +
            weights['recall'] * recall +
            weights['f1'] * f1 -
            weights['fpr'] * fpr)  # Subtract FPR because we want to minimize it

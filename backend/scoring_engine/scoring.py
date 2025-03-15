def calculate_performance(A, B, C, weights=(1, 1, 1)):
    wA, wB, wC = weights
    return (wA * A + wB * B + wC * C) / (wA + wB + wC)

def calculate_cost(D, E, F, weights=(1, 1, 1)):
    wD, wE, wF = weights
    return (wD * (10 - D) + wE * (10 - E) + wF * F) / (wD + wE + wF)

def calculate_training(G, H, I):
    return (G + H + I) / 3

def calculate_integration(J, K, L):
    return (J + K + L) / 3

def calculate_user_experience(M, N, O):
    return (M + N + O) / 3

def calculate_compliance(P, Q):
    return (P + Q) / 2

def calculate_risk(R, S):
    return (R + S) / 2

def calculate_market_adoption(T, U, V):
    return (T + U + V) / 3

def calculate_social_media(AA, AB, AC):
    return (AA + AB + AC) / 3

def calculate_comparative(AD, AE):
    return (AD + AE) / 2

def calculate_ethical(AF, AG, AH):
    return (AF + AG + AH) / 3

def calculate_adoption_risk(AI, AJ):
    return (AI + AJ) / 2

def calculate_market_trends(AK, AL, AM, AN):
    return (AK + AL + AM + AN) / 4

def calculate_overall_score(sub_scores, weights):
    total_weight = sum(weights.values())
    weighted_sum = sum(weights[key] * sub_scores[key] for key in sub_scores)
    return (weighted_sum / total_weight) * 10

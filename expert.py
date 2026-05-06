def diagnose(s):
    if s['fever'] and s['cough'] and s['body_ache'] and s['loss_of_smell']:
        return "COVID-19", "Isolate immediately, consult a doctor, get tested.", "High"

    elif s['fever'] and s['cough'] and s['body_ache'] and s['runny_nose']:
        return "FLU (Influenza)", "Rest, drink fluids, take paracetamol.", "Medium"

    elif s['fever'] and s['chills'] and s['sweating'] and s['headache']:
        return "MALARIA", "Consult a doctor immediately for blood test.", "High"

    elif s['fever'] and s['stomach_pain'] and s['weakness'] and s['headache']:
        return "TYPHOID", "Widal test recommended. Take antibiotics as prescribed.", "High"

    elif s['fever'] and s['joint_pain'] and s['rash'] and s['headache']:
        return "DENGUE", "Monitor platelet count, consult doctor immediately.", "High"

    elif not s['fever'] and s['cough'] and s['runny_nose']:
        return "COMMON COLD", "Rest, stay hydrated, take antihistamines.", "Low"

    elif s['chest_pain'] and s['shortness_of_breath'] and s['sweating']:
        return "HEART ATTACK (Suspected)", "Call emergency services immediately!", "Critical"

    elif s['fever'] and s['stiff_neck'] and s['sensitivity_to_light']:
        return "MENINGITIS (Suspected)", "Emergency hospitalization required.", "Critical"

    elif s['fever'] and s['yellow_skin'] and s['stomach_pain']:
        return "JAUNDICE / HEPATITIS", "Liver function test required. Avoid fatty food.", "High"

    elif s['fever'] and s['cough'] and s['night_sweats'] and s['weight_loss']:
        return "TUBERCULOSIS (TB)", "Visit nearest TB clinic. DOTS therapy may be needed.", "High"

    elif s['shortness_of_breath'] and s['wheezing'] and not s['fever']:
        return "ASTHMA", "Use prescribed inhaler. Avoid triggers. Consult pulmonologist.", "Medium"

    elif s['frequent_urination'] and s['excessive_thirst'] and s['fatigue']:
        return "DIABETES (Suspected)", "Check blood sugar levels. Consult endocrinologist.", "Medium"

    elif s['headache'] and s['dizziness'] and s['blurred_vision']:
        return "HYPERTENSION (High BP)", "Check BP immediately. Reduce salt intake. See doctor.", "Medium"

    elif s['stomach_pain'] and s['vomiting'] and s['diarrhea'] and not s['fever']:
        return "FOOD POISONING", "ORS fluids, rest, avoid solid food for 24 hrs.", "Medium"

    elif s['rash'] and s['itching'] and not s['fever']:
        return "ALLERGIC REACTION / DERMATITIS", "Antihistamines. Avoid allergen. See dermatologist.", "Low"

    else:
        return "UNKNOWN", "Symptoms unclear. Please consult a doctor for proper diagnosis.", "Unknown"


def get_input(question):
    while True:
        ans = input(question + " (yes/no): ").strip().lower()
        if ans in ('yes', 'no'):
            return ans == 'yes'
        print("Please type 'yes' or 'no'.")


def main():
    print("=" * 50)
    print("     MEDICAL EXPERT SYSTEM - SPPU LP-II")
    print("=" * 50)
    print("Answer the following questions carefully.\n")

    questions = {
        'fever':               'Do you have fever?',
        'cough':               'Do you have cough?',
        'body_ache':           'Do you have body ache?',
        'runny_nose':          'Do you have runny nose?',
        'loss_of_smell':       'Do you have loss of smell or taste?',
        'chills':              'Do you have chills?',
        'sweating':            'Do you have excessive sweating?',
        'headache':            'Do you have headache?',
        'stomach_pain':        'Do you have stomach pain?',
        'weakness':            'Do you feel weak or fatigued?',
        'joint_pain':          'Do you have joint or muscle pain?',
        'rash':                'Do you have skin rash?',
        'itching':             'Do you have itching?',
        'chest_pain':          'Do you have chest pain?',
        'shortness_of_breath': 'Do you have shortness of breath?',
        'night_sweats':        'Do you have night sweats?',
        'weight_loss':         'Have you had unexplained weight loss?',
        'yellow_skin':         'Do you have yellowing of skin or eyes?',
        'stiff_neck':          'Do you have stiff neck?',
        'sensitivity_to_light':'Are you sensitive to light?',
        'frequent_urination':  'Do you have frequent urination?',
        'excessive_thirst':    'Do you have excessive thirst?',
        'fatigue':             'Do you feel constant fatigue?',
        'dizziness':           'Do you feel dizzy?',
        'blurred_vision':      'Do you have blurred vision?',
        'vomiting':            'Do you have vomiting?',
        'diarrhea':            'Do you have diarrhea?',
        'wheezing':            'Do you have wheezing while breathing?',
    }

    symptoms = {}
    for key, question in questions.items():
        symptoms[key] = get_input(question)

    disease, recommendation, severity = diagnose(symptoms)

    print("\n" + "=" * 50)
    print("         DIAGNOSIS REPORT")
    print("=" * 50)
    print(f" Diagnosed Condition : {disease}")
    print(f" Severity Level      : {severity}")
    print(f" Recommendation      : {recommendation}")
    print("=" * 50)
    print("NOTE: This is an AI-based expert system.")
    print("Always consult a qualified doctor for confirmation.")
    print("=" * 50)


# Run
main()



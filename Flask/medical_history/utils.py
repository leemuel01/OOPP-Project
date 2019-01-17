from Flask.Models import Admissions, Surgeries, Blood_Transfusions, Allergies
from Flask.medical_history.forms import Previous_Admissions_Form, Previous_Surgeries_Form, \
    Blood_Transfusion_History_Form, Allergy_History_Form

records = {"Admissions": [Admissions, Previous_Admissions_Form()],
               "Surgeries": [Surgeries, Previous_Surgeries_Form()],
               "Blood Transfusions": [Blood_Transfusions, Blood_Transfusion_History_Form()],
               "Allergies": [Allergies, Allergy_History_Form()]}
from datetime import datetime
def bulk_member_onboarding(row):
    data = {
        "membership": row[1],
        "user_obj": {
            "email": row[2],
            "username": row[3],
            "first_name": row[4],
            "last_name": row[5]
        },
        "member_obj": {
            "id_number": row[7],
            "phone_number": row[6],
            "kra_pin": row[8],
            "birth_date": datetime.strptime(row[9], '%m-%d-%Y').date(),
            "gender": row[10],
            "marital_status": row[11],
            "postal_code": row[12],
            "town": row[13],
            "country": row[14],
            "status": row[15]
        },
        "payment_obj": {
            "payment_method": row[16],
            "mpesa_number": row[17],
            "preferred_payment_day": row[18]
        },
        "employment_obj": {
            "employment_status": row[19],
            "employment_sector": row[20],
            "salary": row[21],
            "total_deductions": row[22],
            "employer": row[23],
            "position": row[24],
            "date_employed": datetime.strptime(row[25], '%m-%d-%Y').date(),
            "previous_employer": row[26],
            "previous_salary": row[27]
        },
        "family_obj": {
            "name": row[28],
            "phone_number": row[29],
            "email": row[30],
            "relationship": row[31],
            "birth_date": datetime.strptime(row[32], '%m-%d-%Y').date(),
            "gender": row[33],
            "marital_status": row[34],
            "postal_code": row[35],
            "town": row[36],
            "country": row[37]
        },
        "education_obj": {
            "highest_education_level": row[38],
            "last_school_attended": row[39],
            "year_joined": row[40],
            "graduation_year": row[41],
            "course": row[42],
            "grade": row[43]
        },
        "subscription_obj": {
            "subscription_title": row[44],
            "rate": row[45]
        }
    }
    return data

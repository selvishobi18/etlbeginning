from datetime import datetime

def transform_csv(datas):
    seen_id = []
    
    final_rec = []

    for data in datas:
        emp_id = data["employee_id"]
        processed_rec = {}

        if emp_id not in seen_id:
            seen_id.append(emp_id)
            #process the records
            processed_rec["employee_id"] = data.get("employee_id","Not avail")
            processed_rec["name"] = data.get("name") or "Not avail"
            processed_rec["department"] = data.get("department") or "Not Avail"
            processed_rec["salary"] = float(data.get("salary") or 0)
            processed_rec["email"] = data.get("email") or "Not Avail"
            joining_date = data.get("joining_date")
            if joining_date:
                processed_rec["joining_date"] = datetime.strptime(joining_date,"%Y-%m-%d").date().isoformat()
            else:
                processed_rec["joining_date"] = None    
            processed_rec["process_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(processed_rec)
            final_rec.append(processed_rec)

        else:
            continue

    return final_rec
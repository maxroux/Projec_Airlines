
import requests
import json

url_template = "https://api.lufthansa.com/v1/operations/flightstatus/departures/{airportCode}/{fromDateTime}"

headers = {
    "Authorization": "Bearer rt4cnr4rcdxvk8sf25uwbgmw"
}
try:
    with open("/Users/Chams/Desktop/airline_project/departure_result.json", "r") as json_file:
        previous_results = json.load(json_file)
except FileNotFoundError:
    previous_results = []
results = previous_results
errors = []
airport_codes = ['AAL', 'AAR', 'ABE', 'ABJ', 'ABK', 'ABQ', 'ABV', 'ABZ', 'ACA', 'ACC', 'ACE', 'ACK', 'ACT', 'ACV', 'ACY', 'ADA', 'ADB', 'ADD', 'ADK', 'ADL', 'ADQ', 'ADZ', 'AEP', 'AER', 'AES', 'AEX', 'AGA', 'AGH', 'AGP', 'AGS', 'AGT', 'AGU', 'AHB', 'AHO', 'AIA', 'AJA', 'AJI', 'AJL', 'AJR', 'AJU', 'AKJ', 'AKL', 'ALA', 'ALB', 'ALC', 'ALF', 'ALG', 'ALS', 'ALW', 'AMA', 'AMD', 'AMH', 'AMI', 'AMM', 'AMS', 'ANC', 'ANF', 'ANU', 'AOI', 'AOJ', 'AOK', 'AOR', 'APL', 'APW', 'AQJ', 'AQP', 'ARH', 'ARI', 'ARN', 'ASB', 'ASE', 'ASF', 'ASM', 'ASO', 'ASR', 'ASU', 'ASW', 'ATH', 'ATL', 'ATQ', 'ATW', 'ATZ', 'AUA', 'AUH', 'AUS', 'AUW', 'AVL', 'AVP', 'AWA', 'AWZ', 'AXD', 'AXM', 'AXT', 'AXU', 'AYT', 'AZO', 'AZS', 'BAH', 'BAL', 'BAQ', 'BAV', 'BBA', 'BBI', 'BBK', 'BBO', 'BCN', 'BCO', 'BDA', 'BDL', 'BDO', 'BDQ', 'BDS', 'BEG', 'BEL', 'BER', 'BET', 'BEW', 'BEY', 'BFF', 'BFL', 'BFM', 'BFN', 'BGA', 'BGF', 'BGG', 'BGI', 'BGO', 'BGR', 'BGW', 'BGY', 'BHD', 'BHE', 'BHI', 'BHM', 'BHO', 'BHX', 'BHY', 'BIA', 'BIL', 'BIO', 'BIQ', 'BIS', 'BJL', 'BJM', 'BJR', 'BJV', 'BJX', 'BKI', 'BKK', 'BKO', 'BLA', 'BLL', 'BLQ', 'BLR', 'BLZ', 'BMA', 'BNA', 'BNE', 'BOD', 'BOG', 'BOI', 'BOJ', 'BOM', 'BOO', 'BOS', 'BPN', 'BPS', 'BPT', 'BQH', 'BQN', 'BRC', 'BRE', 'BRI', 'BRM', 'BRN', 'BRO', 'BRQ', 'BRS', 'BRU', 'BRW', 'BSB', 'BSL', 'BTR', 'BTU', 'BTV', 'BUD', 'BUF', 'BUQ', 'BUR', 'BUS', 'BVC', 'BWI', 'BWK', 'BWN', 'BZE', 'BZG', 'BZN', 'BZV', 'CAE', 'CAG', 'CAI', 'CAK', 'CAN', 'CBR', 'CCJ', 'CCP', 'CCS', 'CCU', 'CDG', 'CDR', 'CDV', 'CEB', 'CEC', 'CEI', 'CEZ', 'CFU', 'CGB', 'CGH', 'CGK', 'CGN', 'CGO', 'CGQ', 'CGR', 'CHA', 'CHC', 'CHG', 'CHO', 'CHQ', 'CHS', 'CIC', 'CID', 'CIT', 'CJB', 'CJC', 'CJU', 'CKB', 'CKG', 'CKY', 'CLD', 'CLE', 'CLJ', 'CLL', 'CLO', 'CLT', 'CLY', 'CMB', 'CME', 'CMH', 'CMI', 'CMN', 'CMX', 'CND', 'CNF', 'CNS', 'CNX', 'CNY', 'COD', 'COK', 'COO', 'COR', 'COS', 'COU', 'CPH', 'CPO', 'CPR', 'CPT', 'CRD', 'CRK', 'CRP', 'CRW', 'CSL', 'CSX', 'CTA', 'CTG', 'CTS', 'CTU', 'CUC', 'CUL', 'CUM', 'CUN', 'CUR', 'CUU', 'CUZ', 'CVG', 'CWA', 'CWB', 'CWL', 'CYS', 'CZM', 'CZX', 'DAB', 'DAC', 'DAD', 'DAR', 'DAT', 'DAV', 'DAX', 'DAY', 'DBV', 'DCA', 'DDC', 'DDG', 'DEB', 'DEL', 'DEN', 'DFW', 'DGO', 'DIB', 'DIK', 'DIR', 'DIY', 'DJE', 'DKR', 'DLA', 'DLC', 'DLH', 'DLM', 'DME', 'DMK', 'DMM', 'DMU', 'DNH', 'DNK', 'DNZ', 'DOH', 'DOK', 'DPS', 'DQA', 'DRO', 'DRS', 'DRT', 'DRW', 'DSE', 'DSM', 'DSN', 'DSS', 'DTM', 'DTN', 'DTW', 'DTZ', 'DUB', 'DUD', 'DUR', 'DUS', 'DVL', 'DVO', 'DXB', 'DYG', 'DYU', 'EAR', 'EAT', 'EAU', 'EBB', 'EBJ', 'EBL', 'ECN', 'ECP', 'EDI', 'EDO', 'EFL', 'EGE', 'EGO', 'EJA', 'ELM', 'ELP', 'ELS']

for code in airport_codes:
    url = url_template.format(airportCode=code, fromDateTime="2024-06-09T08:00")
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            results.append({
                "airport_code": code,
                "data": data
            })
        else:
            errors.append({
                "airport_code": code,
                "status_code": response.status_code,
                "reason": response.reason
            })
    except requests.exceptions.RequestException as e:
        errors.append({
            "airport_code": code,
            "error": str(e)
        })

with open("/Users/Chams/Desktop/airline_project/departure_result.json", "w") as json_file:
    json.dump(results, json_file, indent=4)
    
with open("/Users/Chams/Desktop/airline_project/api_errors.json", "w") as json_file:
    json.dump(errors, json_file, indent=4)

print("Les données ont été enregistrées dans departure_result.json")
print("Les erreurs ont été enregistrées dans api_errors.json")
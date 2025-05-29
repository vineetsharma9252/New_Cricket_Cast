from django.shortcuts import render
from django.http import HttpResponse
from joblib import load
import os
# from django.conf import venue_mappings

# Mapping of venues to home teams (assuming team indices match dropdown values)
VENUE_TEAM_MAPPING = {
    1: 3,  # MA Chidambaram Stadium -> Chennai Super Kings
    2: 6,  # Arun Jaitley Stadium -> Delhi Capitals
    3: 9,  # Narendra Modi Stadium -> Gujarat Titans
    4: 1,  # Eden Gardens -> Kolkata Knight Riders
    5: 10, # Ekana Cricket Stadium -> Lucknow Super Giants
    6: 7,  # Wankhede Stadium -> Mumbai Indians
    7: 4,  # PCA Stadium -> Punjab Kings
    8: 5,  # Sawai Mansingh Stadium -> Rajasthan Royals
    9: 2,  # Chinnaswamy Stadium -> Royal Challengers Bangalore
    10: 8, # Rajiv Gandhi Stadium -> Sunrisers Hyderabad
    # Add other venues as needed (default to Neutral if no team)
}

def home(request):
    return render(request, 'home.html')

players = [
        "SC Ganguly",
        "BB McCullum",
        "RT Ponting",
        "DJ Hussey",
        "Mohammad Hafeez",
        "R Dravid",
        "W Jaffer",
        "V Kohli",
        "JH Kallis",
        "CL White",
        "MV Boucher",
        "B Akhil",
        "AA Noffke",
        "P Kumar",
        "Z Khan",
        "SB Joshi",
        "PA Patel",
        "ML Hayden",
        "MEK Hussey",
        "MS Dhoni",
        "SK Raina",
        "JDP Oram",
        "S Badrinath",
        "K Goel",
        "JR Hopes",
        "KC Sangakkara",
        "Yuvraj Singh",
        "SM Katich",
        "IK Pathan",
        "T Kohli",
        "YK Pathan",
        "SR Watson",
        "M Kaif",
        "DS Lehmann",
        "RA Jadeja",
        "M Rawat",
        "D Salunkhe",
        "SK Warne",
        "SK Trivedi",
        "G Gambhir",
        "V Sehwag",
        "S Dhawan",
        "L Ronchi",
        "ST Jayasuriya",
        "DJ Thornely",
        "RV Uthappa",
        "PR Shah",
        "AM Nayar",
        "SM Pollock",
        "Harbhajan Singh",
        "S Chanderpaul",
        "LRPL Taylor",
        "AC Gilchrist",
        "Y Venugopal Rao",
        "VVS Laxman",
        "A Symonds",
        "RG Sharma",
        "SB Styris",
        "AS Yadav",
        "SB Bangar",
        "WPUJC Vaas",
        "RP Singh",
        "WP Saha",
        "LR Shukla",
        "DPMD Jayawardene",
        "S Sohal",
        "B Lee",
        "PP Chawla",
        "WA Mota",
        "Kamran Akmal",
        "Shahid Afridi",
        "DJ Bravo",
        "MA Khote",
        "A Nehra",
        "GC Smith",
        "Pankaj Singh",
        "RR Sarwan",
        "S Sreesanth",
        "VRV Singh",
        "SS Tiwary",
        "DS Kulkarni",
        "R Vinay Kumar",
        "AB Agarkar",
        "M Kartik",
        "I Sharma",
        "AM Rahane",
        "Shoaib Malik",
        "MK Tiwary",
        "KD Karthik",
        "R Bhatia",
        "MF Maharoof",
        "VY Mahesh",
        "TM Srivastava",
        "B Chipli",
        "DW Steyn",
        "DB Das",
        "MK Pandey",
        "HH Gibbs",
        "DNT Zoysa",
        "D Kalyankrishna",
        "SE Marsh",
        "SA Asnodkar",
        "Sohail Tanvir",
        "Salman Butt",
        "BJ Hodge",
        "Umar Gul",
        "AB Dinda",
        "SP Fleming",
        "S Vidyut",
        "JA Morkel",
        "AB de Villiers",
        "LPC Silva",
        "DB Ravi Teja",
        "Misbah-ul-Haq",
        "YV Takawale",
        "RR Raje",
        "PJ Sangwan",
        "Mohammad Asif",
        "GD McGrath",
        "Joginder Sharma",
        "MS Gony",
        "M Muralitharan",
        "M Ntini",
        "DT Patil",
        "A Kumble",
        "S Anirudha",
        "MM Patel",
        "CK Kapugedera",
        "A Chopra",
        "T Taibu",
        "J Arunkumar",
        "PP Ojha",
        "SP Goswami",
        "SR Tendulkar",
        "U Kaul",
        "TM Dilshan",
        "A Mishra",
        "AD Mascarenhas",
        "NK Patel",
        "LA Pomersbach",
        "Iqbal Abdulla",
        "Younis Khan",
        "PM Sarvesh Kumar",
        "DP Vijaykumar",
        "Shoaib Akhtar",
        "Abdur Razzak",
        "H Das",
        "DR Smith",
        "SD Chitnis",
        "CRD Fernando",
        "VS Yeligati",
        "L Balaji",
        "A Mukund",
        "RR Powar",
        "JP Duminy",
        "A Flintoff",
        "T Thushara",
        "JD Ryder",
        "KP Pietersen",
        "T Henderson",
        "Kamran Khan",
        "RS Bopara",
        "CH Gayle",
        "MC Henriques",
        "R Bishnoi",
        "FH Edwards",
        "KV Sharma",
        "PC Valthaty",
        "RJ Quiney",
        "AS Raut",
        "Yashpal Singh",
        "M Manhas",
        "AA Bilakhia",
        "AN Ghosh",
        "BAW Mendis",
        "DL Vettori",
        "MN van Wyk",
        "RE van der Merwe",
        "TL Suman",
        "Shoaib Ahmed",
        "GR Napier",
        "KP Appanna",
        "LA Carseldine",
        "NV Ojha",
        "SM Harwood",
        "M Vijay",
        "SB Jakati",
        "DA Warner",
        "RJ Harris",
        "D du Preez",
        "M Morkel",
        "AD Mathews",
        "J Botha",
        "C Nanda",
        "SL Malinga",
        "Mashrafe Mortaza",
        "A Singh",
        "GJ Bailey",
        "AB McDonald",
        "Y Nagar",
        "SS Shaikh",
        "R Ashwin",
        "Mohammad Ashraful",
        "CA Pujara",
        "OA Shah",
        "Anirudh Singh",
        "Jaskaran Singh",
        "AP Tare",
        "AT Rayudu",
        "R Sathish",
        "R McLaren",
        "AA Jhunjhunwala",
        "P Dogra",
        "A Uniyal",
        "MS Bisla",
        "YA Abdulla",
        "EJG Morgan",
        "JM Kemp",
        "S Tyagi",
        "RS Gavaskar",
        "SE Bond",
        "KA Pollard",
        "S Ladda",
        "DP Nannes",
        "MJ Lumb",
        "DR Martyn",
        "S Narwal",
        "AB Barath",
        "Bipul Sharma",
        "FY Fazal",
        "AC Voges",
        "MD Mishra",
        "UT Yadav",
        "J Theron",
        "SJ Srivastava",
        "R Sharma",
        "Mandeep Singh",
        "KM Jadhav",
        "SW Tait",
        "KB Arun Karthik",
        "KAJ Roach",
        "PD Collingwood",
        "CK Langeveldt",
        "VS Malik",
        "A Mithun",
        "AP Dole",
        "AN Ahmed",
        "RS Sodhi",
        "DE Bollinger",
        "S Sriram",
        "B Sumanth",
        "C Madan",
        "AG Paunikar",
        "MR Marsh",
        "AJ Finch",
        "STR Binny",
        "Harmeet Singh",
        "IR Jaggi",
        "DT Christian",
        "UBT Chand",
        "DJ Jacobs",
        "AL Menaria",
        "MA Agarwal",
        "AUK Pathan",
        "Sunny Singh",
        "JJ van der Wath",
        "R Ninan",
        "S Aravind",
        "DH Yagnik",
        "S Randiv",
        "BJ Haddin",
        "MS Wade",
        "J Syed Mohammad",
        "RN ten Doeschate",
        "TR Birt",
        "AG Murtaza",
        "I Malhotra",
        "L Ablish",
        "AC Blizzard",
        "CA Ingram",
        "S Nadeem",
        "VR Aaron",
        "JEC Franklin",
        "BA Bhatt",
        "Shakib Al Hasan",
        "F du Plessis",
        "RE Levi",
        "GJ Maxwell",
        "KK Cooper",
        "JP Faulkner",
        "HV Patel",
        "DAJ Bracewell",
        "DJ Harris",
        "Ankit Sharma",
        "SP Narine",
        "AA Chavan",
        "GB Hogg",
        "RR Bhatkal",
        "CJ McKay",
        "N Saini",
        "DA Miller",
        "Azhar Mahmood",
        "NLTC Perera",
        "RJ Peterson",
        "KMDN Kulasekara",
        "A Ashish Reddy",
        "V Pratap Singh",
        "Gurkeerat Singh",
        "PA Reddy",
        "P Awana",
        "AD Russell",
        "P Negi",
        "A Chandila",
        "CA Lynn",
        "P Parameswaran",
        "Sunny Gupta",
        "MC Juneja",
        "KK Nair",
        "MDKJ Perera",
        "R Shukla",
        "B Laughlin",
        "AS Rajpoot",
        "JD Unadkat",
        "GH Vihari",
        "Mohammed Shami",
        "BMAJ Mendis",
        "M Vohra",
        "R Rampaul",
        "CH Morris",
        "SV Samson",
        "SMSM Senanayake",
        "BJ Rohrer",
        "KL Rahul",
        "R Dhawan",
        "MG Johnson",
        "Q de Kock",
        "BB Samantray",
        "CM Gautam",
        "X Thalaivan Sargunam",
        "DJG Sammy",
        "MM Sharma",
        "Sandeep Sharma",
        "S Kaul",
        "Sachin Baby",
        "PV Tambe",
        "NM Coulter-Nile",
        "SA Yadav",
        "CJ Anderson",
        "NJ Maddinson",
        "AR Patel",
        "JJ Bumrah",
        "JDS Neesham",
        "SPD Smith",
        "B Kumar",
        "TG Southee",
        "S Rana",
        "MA Starc",
        "BR Dunk",
        "RR Rossouw",
        "KW Richardson",
        "Shivam Sharma",
        "YS Chahal",
        "LMP Simmons",
        "VH Zol",
        "BCJ Cutting",
        "Imran Tahir",
        "WD Parnell",
        "BE Hendricks",
        "S Gopal",
        "M de Lange",
        "R Tewatia",
        "JO Holder",
        "Karanveer Singh",
        "SS Iyer",
        "DJ Hooda",
        "Anureet Singh",
        "KS Williamson",
        "Parvez Rasool",
        "SA Abbott",
        "J Suchith",
        "RG More",
        "HH Pandya",
        "D Wiese",
        "SN Khan",
        "MJ McClenaghan",
        "DJ Muthuswami",
        "PJ Cummins",
        "SN Thakur",
        "CR Brathwaite",
        "MP Stoinis",
        "Ishan Kishan",
        "C Munro",
        "JC Buttler",
        "P Sahu",
        "KH Pandya",
        "AD Nath",
        "MJ Guptill",
        "KJ Abbott",
        "TM Head",
        "NS Naik",
        "RR Pant",
        "SW Billings",
        "KC Cariappa",
        "Swapnil Singh",
        "HM Amla",
        "F Behardien",
        "N Rana",
        "BB Sran",
        "S Kaushik",
        "J Yadav",
        "ER Dwivedi",
        "CJ Jordan",
        "TS Mills",
        "A Choudhary",
        "JJ Roy",
        "Vishnu Vinod",
        "Basil Thampi",
        "CR Woakes",
        "V Shankar",
        "Rashid Khan",
        "C de Grandhomme",
        "Mohammad Nabi",
        "AJ Tye",
        "K Rabada",
        "Kuldeep Yadav",
        "S Badree",
        "AR Bawne",
        "SP Jackson",
        "Ankit Soni",
        "AF Milne",
        "MN Samuels",
        "TA Boult",
        "E Lewis",
        "DL Chahar",
        "MA Wood",
        "RK Singh",
        "DJM Short",
        "BA Stokes",
        "RA Tripathi",
        "K Gowtham",
        "TK Curran",
        "M Markande",
        "B Stanlake",
        "Mujeeb Ur Rahman",
        "Washington Sundar",
        "A Dananjaya",
        "Shubman Gill",
        "Shivam Mavi",
        "Mohammed Siraj",
        "H Klaasen",
        "RK Bhui",
        "JC Archer",
        "PP Shaw",
        "LE Plunkett",
        "Mustafizur Rahman",
        "AD Hales",
        "MK Lomror",
        "M Ashwin",
        "DR Shorey",
        "MM Ali",
        "M Prasidh Krishna",
        "P Chopra",
        "JPR Scantlebury-Searles",
        "Abhishek Sharma",
        "IS Sodhi",
        "SO Hetmyer",
        "S Dube",
        "Navdeep Saini",
        "JM Bairstow",
        "KMA Paul",
        "Rasikh Salam",
        "N Pooran",
        "P Ray Barman",
        "SM Curran",
        "GC Viljoen",
        "Avesh Khan",
        "S Lamichhane",
        "RD Chahar",
        "HF Gurney",
        "SD Lad",
        "AS Joseph",
        "R Parag",
        "MJ Santner",
        "JL Denly",
        "LS Livingstone",
        "KK Ahmed",
        "AJ Turner",
        "Harpreet Brar",
        "SE Rutherford",
        "Y Prithvi Raj",
        "P Simran Singh",
        "JL Pattinson",
        "A Nortje",
        "T Banton",
        "LH Ferguson",
        "D Padikkal",
        "YBK Jaiswal",
        "RD Gaikwad",
        "TU Deshpande",
        "Abdul Samad",
        "PK Garg",
        "JR Philippe",
        "Kartik Tyagi",
        "KL Nagarkoti",
        "CV Varun",
        "I Udana",
        "Ravi Bishnoi",
        "Shahbaz Ahmed",
        "AT Carey",
        "N Jagadeesan",
        "T Natarajan",
        "P Dubey",
        "SS Cottrell",
        "Arshdeep Singh",
        "DR Sams",
        "M Jansen",
        "RM Patidar",
        "KA Jamieson",
        "M Shahrukh Khan",
        "JA Richardson",
        "Lalit Yadav",
        "Virat Singh",
        "FA Allen",
        "C Sakariya",
        "DJ Malan",
        "KS Bharat",
        "PWH de Silva",
        "VR Iyer",
        "GD Phillips",
        "GHS Garton",
        "AK Markram",
        "K Yadav",
        "T Shamsi",
        "NT Ellis",
        "RV Patel",
        "TL Seifert",
        "Anmolpreet Singh",
        "Anuj Rawat",
        "TH David",
        "DP Conway",
        "Tilak Varma",
        "R Powell",
        "PBB Rajapaksa",
        "RA Bawa",
        "OF Smith",
        "A Badoni",
        "PVD Chameera",
        "A Manohar",
        "R Shepherd",
        "DJ Willey",
        "D Pretorius",
        "JM Sharma",
        "VG Arora",
        "Mukesh Choudhary",
        "Umran Malik",
        "D Brevis",
        "B Sai Sudharsan",
        "Ramandeep Singh",
        "HE van der Dussen",
        "SS Prabhudessai",
        "Akash Deep",
        "JR Hazlewood",
        "KR Sen",
        "Aman Hakim Khan",
        "HR Shokeen",
        "Yash Dayal",
        "DJ Mitchell",
        "Shashank Singh",
        "B Indrajith",
        "Harshit Rana",
        "Mohsin Khan",
        "Simarjeet Singh",
        "M Theekshana",
        "AS Roy",
        "Fazalhaq Farooqi",
        "K Kartikeya",
        "RP Meredith",
        "KS Sharma",
        "T Stubbs",
        "R Sanjay Yadav",
        "A Tomar",
        "PN Mankad",
        "OC McCoy",
        "Sikandar Raza",
        "Rahmanullah Gurbaz",
        "KR Mayers",
        "Mukesh Kumar",
        "HC Brook",
        "AU Rashid",
        "C Green",
        "N Wadhera",
        "Arshad Khan",
        "Abishek Porel",
        "Dhruv Jurel",
        "MG Bracewell",
        "MW Short",
        "Mohit Rathee",
        "YV Dhull",
        "A Zampa",
        "Yudhvir Singh",
        "Atharva Taide",
        "Harpreet Singh",
        "Liton Das",
        "PD Salt",
        "Vijaykumar Vyshak",
        "Abdul Basith",
        "Arjun Tendulkar",
        "JP Behrendorff",
        "AJ Hosein",
        "Naveen-ul-Haq",
        "Noor Ahmad",
        "JE Root",
        "KM Asif",
        "MD Shanaka",
        "Sanvir Singh",
        "Vivrant Sharma",
        "DG Nalkande",
        "R Ravindra",
        "SD Hope",
        "Sumit Kumar",
        "Azmatullah Omarzai",
        "Naman Dhir",
        "G Coetzee",
        "SZ Mulani",
        "Sameer Rizvi",
        "SH Johnson",
        "Akash Madhwal",
        "SB Dubey",
        "Mayank Dagar",
        "RJW Topley",
        "A Raghuvanshi",
        "Ashutosh Sharma",
        "Nithish Kumar Reddy",
        "Saurav Chauhan",
        "Kumar Kushagra",
        "BR Sharath",
        "WG Jacks",
        "J Fraser-McGurk",
        "Tanush Kotian",
        "KA Maharaj",
        "Arshad Khan (2)",
        "R Sai Kishore",
        "L Wood",
        "LB Williams",
        "AA Kulkarni",
        "MJ Suthar",
        "RJ Gleeson",
        "Gulbadin Naib",
        "D Ferreira",
        "A Kamboj",
        "T Kohler-Cadmore",
        "Shivam Singh",
        "V Viyaskanth",
        "P Amarnath",
        "B Geeves",
        "Gagandeep Singh",
        "A Nel",
        "AM Salvi",
        "RR Bose",
        "SS Sarkar",
        "RA Shaikh",
        "C Ganapathy",
        "MB Parmar",
        "SB Wagh",
        "ND Doshi",
        "AA Kazi",
        "Anand Rajan",
        "RW Price",
        "TP Sudhindra",
        "BW Hilfenhaus",
        "P Suyal",
        "MG Neser",
        "IC Pandey",
        "K Santokie",
        "JW Hastings",
        "GS Sandhu",
        "Tejas Baroka",
        "SS Agarwal",
        "NB Singh",
        "MJ Henry",
        "K Khejroliya",
        "L Ngidi",
        "CJ Dala",
        "SC Kuggeleijn",
        "S Midhun",
        "O Thomas",
        "S Sandeep Warrier",
        "CJ Green",
        "Monu Kumar",
        "LI Meriwala",
        "Jalaj S Saxena",
        "Akash Singh",
        "IC Porel",
        "PH Solanki",
        "M Pathirana",
        "J Little",
        "RS Hangargekar",
        "NA Saini",
        "Yash Thakur",
        "Suyash Sharma",
        "SSB Magala",
        "D Jansen",
        "Gurnoor Brar",
        "R Goyal",
        "H Sharma",
        "N Burger",
        "KT Maphaka",
        "M Siddharth",
        "MP Yadav",
        "S Joseph",
        "N Thushara",
        "V Kaverappa",
]



def Score_pred(request):
    if request.method == "POST":
        try:
            # Extract and validate POST data
            required_fields = [
                "innings", "venue", "batter_team", "bowler_team", "over",
                "ball", "current_score", "batter_name", "bowler_name", "non_striker_name"
            ]
            data = {}
            for field in required_fields:
                value = request.POST.get(field)
                if not value or not value.isdigit():
                    return render(request, 'Score_pred.html', {
                        "error": f"Invalid or missing {field.replace('_', ' ')}"
                    })
                data[field] = int(value)

            # Validate specific constraints
            if data["batter_team"] == data["bowler_team"]:
                return render(request, 'Score_pred.html', {
                    "error": "Batter and bowler teams must be different"
                })
            if len(set([data["batter_name"], data["bowler_name"], data["non_striker_name"]])) < 3:
                return render(request, 'Score_pred.html', {
                    "error": "Batter, bowler, and non-striker must be different players"
                })
            if not (1 <= data["over"] <= 20):
                return render(request, 'Score_pred.html', {
                    "error": "Over must be between 1 and 20"
                })
            if not (1 <= data["ball"] <= 6):
                return render(request, 'Score_pred.html', {
                    "error": "Ball must be between 1 and 6"
                })
            if data["current_score"] < 0:
                return render(request, 'Score_pred.html', {
                    "error": "Current score cannot be negative"
                })

            # Determine home_team and Neutral
            venue = data["venue"]
            batter_team = data["batter_team"]
            bowler_team = data["bowler_team"]
            home_team = False
            Neutral = True

            if venue in VENUE_TEAM_MAPPING:
                home_team_id = VENUE_TEAM_MAPPING[venue]
                if home_team_id == batter_team:
                    home_team = True
                    Neutral = False
                elif home_team_id == bowler_team:
                    home_team = False
                    Neutral = False

            # Load model
            model_path = "C:/Users/maste/Downloads/fast-API/cricketCast/cricket/src/modelETR.pkl"
            try:
                modelETR = load(model_path)
            except Exception as e:
                return render(request, 'Score_pred.html', {
                    "error": "Failed to load prediction model. Please try again later."
                })

            # Prepare analysis data (ensure this matches model training features)
            analysis_data = [
                data["innings"], data["over"], data["ball"], data["current_score"],
                Neutral, home_team, data["batter_name"], data["bowler_name"],
                data["batter_team"], data["non_striker_name"], data["bowler_team"]
            ]

            # Predict score
            final_score_prediction = int(modelETR.predict([analysis_data])[0])

            return render(request, 'Score_pred.html', {
                "final_score": final_score_prediction,
                "form_submitted": True  # Flag to show prediction and update form
            })
            
            request.session['match_state'] = {
                'current_score': data["current_score"],
                'current_over': data["over"],
                'current_ball': data["ball"]
            }
            
            # Store final score separately
            request.session['final_score'] = final_score_prediction
            
            # Store prediction data if needed
            request.session['prediction_data'] = {
                'innings': data["innings"],
                'venue': data["venue"],
                # [Other prediction parameters]
            }

            return render(request, 'Score_pred.html', {
                "final_score": final_score_prediction,
                "form_submitted": True,
                "current_score": data["current_score"],
                "current_over": data["over"],
                "current_ball": data["ball"],
                # [Other template variables]
            })

        except Exception as e:
            return render(request, 'Score_pred.html', {
                "error": f"An error occurred: {str(e)}"
            })

    return render(request, 'Score_pred.html')

    #     except Exception as e:
    #         return render(request, 'Score_pred.html', {
    #             "error": f"An error occurred: {str(e)}"
    #         })

    # return render(request, 'Score_pred.html')

def update_score(request):
    if request.method == "POST":
        try:
            # Get current match state from session or initialize
            match_state = request.session.get('match_state', {
                'current_score': 0,
                'current_over': 1,
                'current_ball': 1
            })
            
            # Extract update data
            run_taken = int(request.POST.get("run_taken", 0))
            event_type = request.POST.get("event_type", "none")
            extras = int(request.POST.get("extras", 0))
            
            # Validate update data
            if not (0 <= run_taken <= 6):
                return render(request, 'Score_pred.html', {
                    "error": "Runs taken must be between 0 and 6",
                    "form_submitted": True,
                    "current_score": match_state['current_score'],
                    "current_over": match_state['current_over'],
                    "current_ball": match_state['current_ball'],
                    "final_score": request.session.get('final_score', 0)
                })
                
            if extras < 0:
                return render(request, 'Score_pred.html', {
                    "error": "Extras cannot be negative",
                    "form_submitted": True,
                    "current_score": match_state['current_score'],
                    "current_over": match_state['current_over'],
                    "current_ball": match_state['current_ball'],
                    "final_score": request.session.get('final_score', 0)
                })

            # Update ball count (unless it's a wide/noball)
            if event_type not in ["wide", "noball"]:
                match_state['current_ball'] += 1
                if match_state['current_ball'] > 6:
                    match_state['current_ball'] = 1
                    match_state['current_over'] += 1

            # Update score based on event type
            if event_type == "wicket":
                match_state['current_score'] += run_taken + extras
            elif event_type in ["wide", "noball"]:
                match_state['current_score'] += 1 + extras  # 1 run penalty for wide/noball
            else:
                match_state['current_score'] += run_taken + extras

            # Save updated state to session
            request.session['match_state'] = match_state
            
            # Return to the same page with updated values
            return render(request, 'Score_pred.html', {
                "form_submitted": True,
                "current_score": match_state['current_score'],
                "current_over": match_state['current_over'],
                "current_ball": match_state['current_ball'],
                "final_score": request.session.get('final_score', 0),
                # Include original prediction data if needed
                **request.session.get('prediction_data', {})
            })

        except Exception as e:
            return render(request, 'Score_pred.html', {
                "error": f"Update failed: {str(e)}",
                "form_submitted": True,
                "current_score": request.session.get('match_state', {}).get('current_score', 0),
                "current_over": request.session.get('match_state', {}).get('current_over', 1),
                "current_ball": request.session.get('match_state', {}).get('current_ball', 1),
                "final_score": request.session.get('final_score', 0)
            })

    return render(request, 'Score_pred.html', {
        "error": "Invalid request",
        "form_submitted": False
    })
    
    
from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd

# Placeholder model for score prediction
from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Placeholder model for score prediction
def predict_score(input_data):
    weights = {
        'inning': 10,
        'over': 5,
        'ball': 2,
        'score': 1,
        'batter_code': 0.5,
        'bowler_code': 0.3,
        'non_striker_code': 0.2,
        'batting_team_code': 3,
        'bowling_team_code': 3
    }
    score = sum(input_data[key] * weights.get(key, 0) for key in input_data if key in weights)
    if input_data.get('Neutral', False):
        score += 10
    if input_data.get('is_home_team', False):
        score += 5
    return round(score, 2)

# Player list (abbreviated; use the full list provided)
# players = [
#     "SC Ganguly", "BB McCullum", "RT Ponting", "DJ Hussey", "Mohammad Hafeez", "R Dravid",
#     # ... (include the full list here)
#     "V Kaverappa"
# ]

# Assign points to players
def get_player_cost(player_index):
    # Assign costs based on player index (you can modify this logic)
    if player_index < 50:  # Top tier players
        return 150
    elif player_index < 100:  # Premium players
        return 120
    elif player_index < 200:  # Good players
        return 90
    elif player_index < 300:  # Average players
        return 70
    elif player_index < 400:  # Budget players
        return 50
    else:  # Low-cost players
        return 30

# Create player costs dictionary
player_costs = {player: get_player_cost(i) for i, player in enumerate(players)}


from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def fantasy_game(request):
    if request.method == 'POST':
        team1_players = request.POST.getlist('team1[]')
        team2_players = request.POST.getlist('team2[]')

        # Validate team sizes
        if len(team1_players) != 11 or len(team2_players) != 11:
            return JsonResponse({'error': 'Each team must have exactly 11 players'}, status=400)

        # Check for duplicates
        duplicates = set(team1_players).intersection(set(team2_players))
        if duplicates:
            return JsonResponse({
                'error': f'Duplicate players selected: {", ".join(duplicates)}. Players cannot be in both teams.'
            }, status=400)

        # Validate players exist
        for player in team1_players + team2_players:
            if player not in players:
                return JsonResponse({'error': f'Invalid player: {player}'}, status=400)

        # Calculate total costs for teams
        team1_cost = sum(player_costs[player] for player in team1_players)
        team2_cost = sum(player_costs[player] for player in team2_players)

        # Validate budget
        if team1_cost > 1000:
            return JsonResponse({
                'error': f'Player 1 exceeded budget (1000 points). Current team cost: {team1_cost}'
            }, status=400)
        if team2_cost > 1000:
            return JsonResponse({
                'error': f'Player 2 exceeded budget (1000 points). Current team cost: {team2_cost}'
            }, status=400)

        # Rest of your prediction logic remains the same...
        team1_total_score = 0
        team2_total_score = 0

        # Team 1 batting vs Team 2 bowling
        for batter in team1_players:
            batter_code = players.index(batter) + 1
            for bowler in team2_players:
                bowler_code = players.index(bowler) + 1
                non_striker = team1_players[0] if team1_players[0] != batter else team1_players[1]
                non_striker_code = players.index(non_striker) + 1
                input_data = {
                    'inning': 2,
                    'over': 18,
                    'ball': 6,
                    'score': 120,
                    'Neutral': True,
                    'is_home_team': False,
                    'batter_code': batter_code,
                    'bowler_code': bowler_code,
                    'non_striker_code': non_striker_code,
                    'batting_team_code': 10,
                    'bowling_team_code': 7
                }
                score = predict_score(input_data)
                team1_total_score += score

        # Team 2 batting vs Team 1 bowling
        for batter in team2_players:
            batter_code = players.index(batter) + 1
            for bowler in team1_players:
                bowler_code = players.index(bowler) + 1
                non_striker = team2_players[0] if team2_players[0] != batter else team2_players[1]
                non_striker_code = players.index(non_striker) + 1
                input_data = {
                    'inning': 2,
                    'over': 18,
                    'ball': 6,
                    'score': 120,
                    'Neutral': True,
                    'is_home_team': False,
                    'batter_code': batter_code,
                    'bowler_code': bowler_code,
                    'non_striker_code': non_striker_code,
                    'batting_team_code': 7,
                    'bowling_team_code': 10
                }
                score = predict_score(input_data)
                team2_total_score += score

        winner = "Player 1" if team1_total_score > team2_total_score else "Player 2" if team2_total_score > team1_total_score else "Tie"

        return render(request, 'fantasy_game.html', {
            'players': players,
            'player_costs': player_costs,
            'team1_players': team1_players,
            'team2_players': team2_players,
            'team1_score': round(team1_total_score, 2),
            'team2_score': round(team2_total_score, 2),
            'team1_cost': team1_cost,
            'team2_cost': team2_cost,
            'winner': winner
        })

    return render(request, 'fantasy_game.html', {
        'players': players,
        'player_costs': player_costs
    })
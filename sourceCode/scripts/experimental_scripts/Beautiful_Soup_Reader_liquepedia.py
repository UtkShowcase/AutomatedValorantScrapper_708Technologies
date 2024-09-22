import pandas as pd
import numpy as np
from bs4 import BeautifulSoup



COLUMNS = ["tournament_name","tournament_date","tournament_prize_pool","tournament_location_country","tournament_number_of_teams","tournament_winner_team","tournament_runner_team"]



def extractTorunamentInformation(grid_row):


    
    data = dict()
    
    
    try:
    
        data["tournament_name"] = grid_row.find("div",{"class","gridCell Tournament Header"}).find("a",recursive=False).decode_contents().strip()
        
        
        data["tournament_date"] = grid_row.find("div",{"class":"gridCell EventDetails Date Header"}).decode_contents().strip()
        

        data["tournament_prize_pool"] = grid_row.find("div",{"class":"gridCell EventDetails Prize Header"}).decode_contents().strip()

        
        data["tournament_location_country"] =  grid_row.find("div",{"class":"gridCell EventDetails Location Header"}).find("img").get("title").strip()
        
        
        data["tournament_number_of_teams"] = grid_row.find("div",{"class":"gridCell EventDetails PlayerNumber Header"}).find("span").decode_contents().strip()
        
        
        data["tournament_winner_team"] = grid_row.find("div",{"class":"gridCell Placement FirstPlace"}).find("span",{"class":"name"}).find("a").get("title")
        
        
        data["tournament_runner_team"] = grid_row.find("div",{"class":"gridCell Placement SecondPlace"}).find("span",{"class":"name"}).find("a").get("title")


    except Exception as e:
        return None

    return data




def main(INPUT_HTML_LOC,OUTPUT_LOC):
    
    
    
    global COLUMNS
    main_DF = pd.DataFrame(columns=COLUMNS)
    
    
    with open(INPUT_HTML_LOC,"r",encoding="utf8",errors="ignore") as f:
        html = f.read()
    soup = BeautifulSoup(html,"html.parser")
    
    
    match_cards = soup.find_all("div",{"class":"gridTable tournamentCard Tierless NoGameIcon"})

    
    for match_card in match_cards:
        
        
        grid_rows = match_card.find_all("div",{"class":"gridRow"})
        for grid_row in grid_rows:
            
            
            data = extractTorunamentInformation(grid_row=grid_row)
            
            if not data is None:
                
                main_DF.loc[len(main_DF)] = data
        
    
    main_DF.to_csv(OUTPUT_LOC,index=True)
        
    


if __name__ == "__main__":
    
    main(r"D:\ValorantScrappingProject\data\team_list.html",r"D:\AutomatedValorantScarper\workingdata\output_data\output.csv") 
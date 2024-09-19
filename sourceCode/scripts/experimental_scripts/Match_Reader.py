# Importing all the Dependencies

import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup
import sys
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)




# Initializing The Array Containing the Column Names for the Extracted CSV Data
COLUMNS =["Team1" ,"Team2","Map","Map_Duration","Team1_Map_Score","Team1_Number_Of_CT_Rounds","Team1_Number_Of_T_Rounds","Team2_Map_Score","Team2_Number_Of_CT_Rounds","Team2_Number_Of_T_Rounds","Player_Name","Agent_Played","VLR_Total_Rating","VLR_CT_Rating","VLR_T_Rating","Total_ACS","CT_ACS","T_ACS","Total_Kills","CT_Kills","T_Kills","Total_Deaths","CT_Deaths","T_Deaths","Total_Assists","CT_Assists","T_Assists","Total_ADR","CT_ADR","T_ADR","Total_HeadShot%","CT_HeadShot%","T_HeadShot%","Total_First_Kills","CT_First_Kills","T_First_Kills","Total_First_Deaths","CT_First_Deaths","T_First_Deaths"]




def read_from_row_html(row_html):
    """This Method reads the Data Using Beautiful Soup from the Rows Inside the MAP_HTML from its Respective Match HTML

    Args:
        row_html : HTML Code for Each Row Inside the Match HTML
    """
    
    
    
    def filer_all_stats(el):
        """Nested Function Used For Matching the name 'mod-stat'
           Used For Beautiful Soup `find_all()` Matching.
        """
        attr = el.attrs.get('class')
        return attr is not None and ' '.join(attr) == 'mod-stat'


    # Intializing An Emply Flag Dictionary which will store the Data Extracted Form HTML in the Required Key:Value Form
    # It will be Furthered Stored Into An Pandas DataFrame
    data = dict()
    
    
    # Extracting Player Name and Agent Played
    data["Player_Name"] = row_html.find_all("td",{"class":"mod-player"})[0].find("div",{"class":"text-of"}).decode_contents().strip()
    agent = row_html.find("td",{"class":"mod-agents"}).find("span").decode_contents().strip().split()[-1]
    data["Agent_Played"] = agent[agent.index('"')+1:agent.rindex('"')]
    
    
    # Extracting the Player's Total_Kills ,CT_Kills ,T_Kills 
    kills_html = row_html.find("td",{"class":"mod-stat mod-vlr-kills"})
    data["Total_Kills"] = kills_html.find("span",{"class":"side mod-side mod-both"}).decode_contents().strip()
    data["CT_Kills"] = kills_html.find("span",{"class":"side mod-side mod-ct"}).decode_contents().strip()
    data["T_Kills"] = kills_html.find("span",{"class":"side mod-side mod-t"}).decode_contents().strip()


    # Extracting the Player's Total_Deaths,CT_Deaths,T_Deaths
    deaths_html = row_html.find("td",{"class":"mod-stat mod-vlr-deaths"})
    data["Total_Deaths"] = deaths_html.find("span",{"class":"side mod-both"}).decode_contents().strip()
    data["CT_Deaths"] =  deaths_html.find("span",{"class":"side mod-ct"}).decode_contents().strip()
    data["T_Deaths"] = deaths_html.find("span",{"class":"side mod-t"}).decode_contents().strip()


    # Extracting the Player's Total_Assists,CT_Assists,T_Assists
    assists_html = row_html.find("td",{"class":"mod-stat mod-vlr-assists"})
    data["Total_Assists"] = assists_html.find("span",{"class":"side mod-both"}).decode_contents().strip()
    data["CT_Assists"] = assists_html.find("span",{"class":"side mod-ct"}).decode_contents().strip()
    data["T_Assists"] = assists_html.find("span",{"class":"side mod-t"}).decode_contents().strip()


    # Extracting the Players Total_First_Kills,CT_First_Kills,T_First_Kills
    firstkill_html = row_html.find("td",{"class":"mod-stat mod-fb"})
    data["Total_First_Kills"] = firstkill_html.find("span",{"class":"side mod-both"}).decode_contents().strip()
    data["CT_First_Kills"] = firstkill_html.find("span",{"class":"side mod-ct"}).decode_contents().strip()
    data["T_First_Kills"] = firstkill_html.find("span",{"class":"side mod-t"}).decode_contents().strip()


    # Extracting the Players Total_First_Deaths, CT_First_Deaths, T_First_Deaths
    firstdeath_html = row_html.find("td",{"class":"mod-stat mod-fd"})
    data["Total_First_Deaths"] = firstdeath_html.find("span",{"class":"side mod-both"}).decode_contents().strip()
    data["CT_First_Deaths"] = firstdeath_html.find("span",{"class":"side mod-ct"}).decode_contents().strip()
    data["T_First_Deaths"] = firstdeath_html.find("span",{"class":"side mod-t"}).decode_contents().strip()

    # Extracting The HTML Containing the Stats Part
    stats_html = row_html.find_all(filer_all_stats)


    # Extracting the Player's VL_Total_Rating ,VLR_CT_Rating ,VLR_T_Rating
    data["VLR_Total_Rating"] = stats_html[0].find("span",{"class":"side mod-side mod-both"}).decode_contents().strip()
    data["VLR_CT_Rating"] = stats_html[0].find("span",{"class":"side mod-side mod-ct"}).decode_contents().strip()
    data["VLR_T_Rating"] = stats_html[0].find("span",{"class":"side mod-side mod-t"}).decode_contents().strip()


    # Extracting the Player's Total_ACS, CT_ACS, T_ACS
    data["Total_ACS"] = stats_html[1].find("span",{"class":"side mod-side mod-both"}).decode_contents().strip()
    data["CT_ACS"] = stats_html[1].find("span",{"class":"side mod-side mod-ct"}).decode_contents().strip()
    data["T_ACS"] = stats_html[1].find("span",{"class":"side mod-side mod-t"}).decode_contents().strip()


    # Extracting the Player's Total_ADR, CT_ADR, T_ADR
    data["Total_ADR"] = stats_html[3].find("span",{"class":"side mod-both"}).decode_contents().strip()
    data["CT_ADR"] = stats_html[3].find("span",{"class":"side mod-ct"}).decode_contents().strip()
    data["T_ADR"] = stats_html[3].find("span",{"class":"side mod-t"}).decode_contents().strip()


    # Extracting the Player's Total_HeadShot%, CT_Headshot%, T_HeadShot%
    data["Total_HeadShot%"] = stats_html[4].find("span",{"class":"side mod-both"}).decode_contents().strip()
    data["CT_HeadShot%"] = stats_html[4].find("span",{"class":"side mod-ct"}).decode_contents().strip()
    data["T_HeadShot%"] = stats_html[4].find("span",{"class":"side mod-t"}).decode_contents().strip()

    # Returning the Filled Data Dictionary
    return data




def read_from_map_html(map_html):
    """This Method reads the Data Using Beautiful Soup from the MAP_HTML from its Respective Match HTML

    Args:
        map_html : HTML Code For Each Map Inside the Match HTML
    """
    
    
    
    def read_Team_Header_Data(tmhd_html):
        """Nested Method to Read the Team's Name,Score,mod-t,mod-ct for the HTML File Containing It.

        Args:
            tmhd_html : HTML Code form which we Require to Extract the Respective Data

        Returns:
            Return Values of the Extracted Team's Name,Score,mod-t,mod-ct
        """
        
        
        team_name = tmhd_html.find("div",{"class":"team-name"}).decode_contents().strip()
        team_map_score = tmhd_html.find("div",{"class":"score"}).decode_contents().strip()
        team_ct_rounds = tmhd_html.find("span",{"class":"mod-t"}).decode_contents().strip()
        team_t_rounds = tmhd_html.find("span",{"class":"mod-ct"}).decode_contents().strip()
        return team_name,team_map_score,team_ct_rounds,team_t_rounds


    # Initalizing An Empty DataFrame which Columns as the STATIC Columns Described In the Module Variable(COLUMNS) 
    df = pd.DataFrame(columns=COLUMNS)
    
    
    # Intializing An Emply Flag Dictionary which will store the Data Extracted Form MAP_HTML in the Required Key:Value Form
    # It will be Furthered Stored Into An Pandas DataFrame
    data = dict()
    
    
    # Extracting the Header HTML Code
    header = map_html.find("div",{"class":"vm-stats-game-header"}).find_all('div', recursive=False)
    
    
    # Extracting Each Team's Name,Score,mod-t,mod-ct Using the Above Nested Method
    team_1 = read_Team_Header_Data(header[0])
    team_2 = read_Team_Header_Data(header[-1])
    
    
    # Unpacking and Assigning the Above Extracted Information in an Proper Way into the Flag Dictionary
    data["Team1"] = team_1[0]
    data["Team1_Map_Score"] = team_1[1]
    data["Team1_Number_Of_CT_Rounds"] = team_1[2]
    data["Team1_Number_Of_T_Rounds"] = team_1[3]


    # Unpacking And Assigning the Above Extracted Information in an Proper Way into the Flag Dicitonary
    data["Team2"] = team_2[0]
    data["Team2_Map_Score"] = team_2[1]
    data["Team2_Number_Of_CT_Rounds"] = team_2[2]
    data["Team2_Number_Of_T_Rounds"] = team_2[3]

    
    # Extracting the Map's Duration and Map(Map Name)
    data["Map_Duration"] = header[1].find("div",{"class":"map-duration ge-text-light"}).decode_contents().strip()
    map = header[1].find_all('div', recursive=False)[0].find("span")
    if map.find("span") == None:
        data["Map"] = map.decode_contents().strip()
    else:
        map.span.decompose()
        data["Map"] = map.decode_contents().strip()


    # Finding All Map's HTML and Iterating Over Each
    for g in map_html.find_all("tbody"):
        
        trs = g.find_all("tr")  # Extracting All Rows HTML
        
        for tr in trs: #Iterating Over Each Row HTML 
            
            row_data = read_from_row_html(tr) # Extracting Data From Row HTML Using the Above User-Defined Method
            row_data.update(data) # Combining the Row Data Dictionary with the Dictionary containing the Map Details
            df.loc[len(df)] = row_data # Adding a New Row at the End of the DataFrame



    # Return the Collected DataFrame
    return df




def main(MATCH_HTML_LOC,OUTPUT_LOC):
    """This Method Reads Full Data from the MATCH HTML(including every map,rows).

    Args:
        MATCH_HTML_LOC : The Input Location of the Match's HTML.
        OUTPUT_LOC : The Output Location in which we want to store the 
    """

    

    def filer_all_maps(el):
        """Nested Function Used For Matching the name 'vm-stats-game'
           Used For Beautiful Soup `find_all()` Matching.
        """
        
        attr = el.attrs.get('class')
        return attr is not None and ' '.join(attr) == 'vm-stats-game'


    # Opening the HTML File and Storing Its Content
    with open(MATCH_HTML_LOC,"r",encoding="utf-8") as f:
        html = f.read()


    # Initializing the the HTML inot Beautiful Soup Object 
    soup = BeautifulSoup(html,"html.parser")
    
    
    # Extracting all the Map HTML 
    map_html_array = soup.find("div",{"class":"vm-stats-container"}).find_all(filer_all_maps)


    # Initializing an Empty Flag List which will be storing the Whole Extracted Data(DataFrames) for Each Map's which will then further be concated
    maps_df = list()
    
    
    # Iterating Over Each Map HTML
    for map_html in map_html_array: 
        
        # Extracting the Whole Data From the Respective Map HTML and Storing the result Data(DataFrame) in the Flag List
        maps_df.append(read_from_map_html(map_html))  


    # Post-Processing the Full Result and Storing in the Respective OUTPUT LOC 
    result = pd.concat(maps_df,axis=0)
    result.reset_index(inplace=True,drop=True)
    result.to_csv(OUTPUT_LOC,index=True)
    print(f"The Data Saved Inside :-\n{OUTPUT_LOC}")


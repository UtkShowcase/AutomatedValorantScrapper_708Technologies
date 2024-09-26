import Selenium_Html_Extractor_vlrgg
import Beautiful_Soup_Reader_vlrgg
import Selenium_Html_Extractor_liquepedia
import Beautiful_Soup_Reader_liquepedia
import pathlib
import os
import pandas as pd




def main():
    
    
    
    main_DF = list()
    
    HTML_SAVING_DIR_LOC = pathlib.Path.cwd().parent.parent.parent.joinpath("workingdata","html_data")
    OUTPUT_SAVING_DIR_LOC = HTML_SAVING_DIR_LOC.parent.joinpath("output_data")
    
    OUTPUT_DATA_LOC = HTML_SAVING_DIR_LOC.parent.joinpath("output_data","valorant_vlr_output_main_data.csv")
    
    
    print("<----------------------------------------->")
    print("Extracting HTML Using Selenium from liquepedia valorant")
    
    
    output_html_liquepedia_file_path = HTML_SAVING_DIR_LOC.joinpath("liquipedia.html")
    Selenium_Html_Extractor_liquepedia.main(output_html_liquepedia_file_path)
    
    print("Extracted from The Liquepedia HTML")
    print("<----------------------------------------->")
    
    output_csv_liquepedia_file_path = OUTPUT_SAVING_DIR_LOC.joinpath("liquepedia.csv")
    Beautiful_Soup_Reader_liquepedia.main(INPUT_HTML_LOC=output_html_liquepedia_file_path,OUTPUT_LOC=output_csv_liquepedia_file_path)
    
    
    print("<----------------------------------------->")
    
    
    '''
    match_url_link = r"https://www.vlr.gg/event/matches/1015/valorant-champions-2022/?series_id=2184"
    
    
    print("<----------------------------------------->")
    print(f"Extracting HTML Using Selenuim form weburl :- {match_url_link}\n\n")
    
    
    Selenium_Html_Extractor_vlrgg.main(match_url_link=match_url_link,HTML_SAVING_DIR_LOC=HTML_SAVING_DIR_LOC)
    
    
    print(f"\n\nExtracted all the HTML Using Selenium from weburl :- {match_url_link}")
    print("<----------------------------------------->")
    
    
    print("<----------------------------------------->")
    print("Extracting CSV Data Using Beautiful Soup from the Above Created HTML Files\n\n")
    
    
    files = os.listdir(HTML_SAVING_DIR_LOC)
    for file in files:
        
        
        print(f"<----------------------------------------->")
        print(f"Reading the HTML File :- {file}")
        
        file_path = HTML_SAVING_DIR_LOC.joinpath(file)
        main_DF.append(Beautiful_Soup_Reader_vlrgg.main(file_path))
        

        print(f"Extracted from the HTML File :- {file}")
        print(f"<----------------------------------------->")
        
    result = pd.concat(main_DF,axis=0)
    result.reset_index(inplace=True,drop=True)
    result.to_csv(OUTPUT_DATA_LOC,index=True)
    
    print(f"Extracted All the CSV Data and Stored :- {OUTPUT_DATA_LOC}")
    print("<----------------------------------------->")'''
        
        
if __name__ == "__main__":
    
    main()
    
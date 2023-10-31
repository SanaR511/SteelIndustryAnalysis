*importing data;
data work.steel;
set work.steel;
drop date;

*Ordering variables to categorize them for graphics;
					    
	
data work.steel1;
	set work.steel;
	if Day_of_week = "Monday" then day = 0;
	else if Day_of_week = "Tuesday" then day = 1;
	else if Day_of_week = "Wednesday" then day = 2;
	else if Day_of_week = "Thursday" then day = 3;
	else if Day_of_week = "Friday" then day = 4;
	else if Day_of_week = "Saturday" then day = 5;
	else day = 6;
	
	if Load_Type = "Light_Load" then load = "A";
	else if Load_Type = "Medium_Load" then load = "B";
	else if Load_Type = "Maximum_Load" then load = "C";
	else load = "D";
	

proc format;
	value nameDay 	    0 = "Monday"       /***levelsOxygen can be named anything***/
				        1 = "Tuesday"
					    2 = "Wednesday"
					    3 = "Thursday"
					    4 = "Friday"
					    5 = "Saturday"
					    6 = "Sunday";
	value $loadAmount   "A" = "Light Load"
	                    "B" = "Medium Load"
	                    "C" = "Maximum Load";
	
data work.steelCat;
	set work.steel1;
	format day nameDay. load $loadAmount.;
	
*Seeing the frequencies;
proc freq data=work.steelCat;
	tables day load;	
	title "Table: Frequency of day Categories";
	
*Boxplot for days;
proc sgplot data=work.steelCat;
    vbox Usage_kWh / category = day;
    title "Figure 1: Usage_kWh by Day of the Week Boxplot";
    
*Boxplot for load;
proc sgplot data=work.steelCat;
    vbox Usage_kWh / category = load;
    title "Figure 2: Usage_kWh by Load Type Boxplot";
    
/*proc glm data = work.steel;
class 'Lagging_Current_Reactive.Power_k'n 'Leading_Current_Reactive_Power_k'n 'CO2(tCO2)'n 'Lagging_Current_Power_Factor'n 'Leading_Current_Power_Factor'n NSM WeekStatus Day_of_week Load_Type;
model Usage_kWh = 'Lagging_Current_Reactive.Power_k'n 'Leading_Current_Reactive_Power_k'n 'CO2(tCO2)'n 
'Lagging_Current_Power_Factor'n 'Leading_Current_Power_Factor'n NSM WeekStatus Day_of_week Load_Type/solution;
run; */

Proc Reg data = work.steel;
id 'Lagging_Current_Reactive.Power_k'n 'Leading_Current_Reactive_Power_k'n 'CO2(tCO2)'n 'Lagging_Current_Power_Factor'n 'Leading_Current_Power_Factor'n NSM;
model Usage_kWh = 'Lagging_Current_Reactive.Power_k'n 'Leading_Current_Reactive_Power_k'n 'CO2(tCO2)'n 
'Lagging_Current_Power_Factor'n 'Leading_Current_Power_Factor'n NSM /CLM CLI alpha=.05;
					    

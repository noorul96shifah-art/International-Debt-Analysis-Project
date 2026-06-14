import streamlit as st
import pandas as pd
import  mysql.connector 

#------------sql connection------------

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="nyha1623@",
    database="debt_db"
)

st.title(" 🌎 International Debt Analysis")

st.subheader(" 💻 SQL Queries")

query={
  
    "1.Retrieve all distinct country names from the dataset":
    "select DISTINCT Country_Name from foodnote_data",

    "2.Count the total number of countries available":
    "select count(*) country_name= from country_series",

    "3.Find the total number of indicators present":
    "select count(*) Indicator_Name from seriesmeta_data",

    "4.Display the first 10 records of the dataset":
    "select * from countrymeta_data limit 10",

    "5.Calculate the total global debt":
    "select sum(debt) as Total_global_Debt from allcountry_data",

    "6.List all unique indicator names":
    "select distinct Indicator_Name from seriesmeta_data",

    "7.Find the number of records for each country":
    """select country_name, count(*) as Record_Counts from allcountry_data
       group by country_name
   """,

    "8.Display all records where debt is greater than 1 billion USD":
    "select * from allcountry_data where debt > 1000000000",

    "9.Find the minimum, maximum, and average debt values":
    """select country_name, sum(debt) as Total_Debt from allcountry_data
       group by country_name
       order by Total_Debt desc limit 10
    """,

    "10.Count total number of records in the dataset":
    """select sm.Indicator_Name,sum(ac.debt) as Total_Debt 
       from allcountry_data ac
       join seriesmeta_data sm
       on ac.series_code=sm.Code
       group by Indicator_Name 
       order by Total_Debt  desc limit 10
    """,

    "11.Find the total debt for each country":
   """select country_name,sum(debt) as Total_Debt from allcountry_data
      group by country_name
    """,

    "12.Display the top 10 countries with the highest total debt":
    """select country_name, sum(debt) as Total_Debt from allcountry_data
       group by country_name
       order by Total_Debt desc limit 10
    """,

    "13.Find the average debt per country":
    """select country_name, avg(debt) as Avg_Debt from allcountry_data
        group by country_name
    """,

    "14.Calculate total debt for each indicator":
    """select sm.Indicator_Name,sum(ac.debt) as Total_Debt 
       from allcountry_data ac
       join seriesmeta_data sm
       on ac.series_code=sm.Code
       group by Indicator_Name
    """,

    "15.Identify the indicator contributing the highest total debt":
    """select sm.Indicator_Name,sum(ac.debt) as Total_Debt 
       from allcountry_data ac
       join seriesmeta_data sm
       on ac.series_code=sm.Code
       group by Indicator_Name
       order by Total_Debt desc limit 1
    """,

    "16.Find the country with the lowest total debt":
    """select country_name,sum(debt) as TotaL_Debt 
       from allcountry_data
       group by country_name
       order by Total_Debt asc limit 1
    """,

    "17.Calculate total debt for each country and indicator combination":
    """select sm.Indicator_Name,sum(ac.debt) as Total_Debt 
       from allcountry_data ac
       join seriesmeta_data sm
       on ac.series_code=sm.Code
       group by Indicator_Name
       order by Total_Debt desc
    """,

    "18.Count how many indicators each country has":
    """select ac.country_name,count(distinct sm.Indicator_Name) as Indicator_count
       from allcountry_data ac
       join seriesmeta_data sm
       on ac.series_code=sm.Code
       group by country_name
      order by Indicator_count
    """,

    "19.Display countries whose total debt is above the global average":
    """select country_name, sum(debt) as Total_Debt
       from allcountry_data
       group by country_name
       having Total_Debt >
    (
       select avg(debt) as Global_Debt
       from allcountry_data
    )
    """,

    "20.Rank countries based on total debt (highest to lowest":
    """select country_name, sum(debt) as Total_Debt,
       rank() over (order by sum(debt)  desc) as Country_Rank
       from allcountry_data
       group by country_name
    """,

    "21.Find the top 5 indicators contributing most to global debt":
    """select sm.Indicator_Name,sum(ac.debt) as Total_Debt 
       from allcountry_data ac
       join seriesmeta_data sm
       on ac.series_code=sm.Code
       group by Indicator_Name
       order by Total_Debt desc limit 5
    """,

    "22.Calculate percentage contribution of each country to total global debt":
    """select country_name,sum(debt) as Country_Debt,
       round(
       (sum(debt) * 100.0)/
       (select sum(debt) from allcountry_data),
       2) as Contribution_Percentage
       from allcountry_data
       group by country_name
       order by Contribution_Percentage desc;
    """,

    "23.Identify the top 3 countries for each indicator based on debt":
    """select * from (
       select sm.Indicator_Name,ac.debt ,ac.country_name,
       rank() over(partition by sm.Indicator_Name order by ac.debt desc) as Rnk 
       from allcountry_data ac
       join seriesmeta_data sm
       on ac.series_code=sm.Code
       )as t
       where Rnk <=3
    """,

    "24.Find the difference between maximum and minimum debt for each country":
    """select country_name, max(debt)-min(debt) as Debt_Difference
       from allcountry_data
       group by country_name
    """,

    "25.Create a view for the top 10 countries with highest debt":
    """select country_name, sum(debt) as Total_Debt
       from allcountry_data
       group by country_name
       order by country_name desc limit 10;
    """,

    """26.Categorize countries into:
    High Debt
    Medium Debt
    Low Debt (based on thresholds)""":
    """select country_name, sum(debt) as Total_Debt,
       case
       when sum(debt) > 10000000000000 then 'High Debt'
       when sum(debt) = 10000000000000 then 'Medium Debt'
       else 'Low Debt'
       end as Debt_Category
       from allcountry_data
       group by country_name;
    """,

    "27.Use window functions to calculate cumulative debt per country":
    """select country_name,debt, sum(debt) over(partition by country_name order by debt) as cumulative_Debt
       from allcountry_data
    """,

    "28.Find indicators where average debt is higher than overall average debt":
    """select sm.Indicator_Name,ac.country_name,avg(ac.debt) as Avg_Debt 
       from allcountry_data ac
       join seriesmeta_data 
       on ac.seies_code=sm.Code
       group by sm.Indicator_Name
       having avg(ac.debt) > 
       ( select avg(ac.debt) from allcountry_data)
    """,  

    "29.Identify countries contributing more than 5% of global debt":
    """select country_name, sum(debt) as Total_Debt
       from allcountry_data
       group by country_name
       having sum(debt) > 
       0.05 * (select sum(debt) from allcountry_data)
    """,

    "30.Find the most dominant indicator (highest contribution) for each country":
    """select country_name,Indicator_Name,Total_Debt
       from (
       select sm.Indicator_Name,sum(ac.debt) as Total_Debt ,ac.country_name,
       row_number() over(partition by ac.country_name
       order by sum(ac.debt) desc) as Rnk 
       from allcountry_data ac
       join seriesmeta_data sm
       on ac.series_code=sm.Code
       group by ac.country_name,sm.Indicator_Name
       )as t
       where Rnk=1
       """
}



selected_query=st.selectbox("Choose Query",list(query))

if st.button("Run query"):

   df=pd.read_sql(query[selected_query],conn)

   st.dataframe(df)

   conn.close()
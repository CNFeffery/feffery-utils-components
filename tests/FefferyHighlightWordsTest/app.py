if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyHighlightWords(
            # caseSensitive=True,
            style={
                'fontSize': '20px'
            },
            highlightStyle={
                'background': '#c7e0f4'
            },
            unhighlightStyle={
                'color': '#c8c6c4'
            },
            useRegex=True,
            searchWords=['\w{12,}'],
            textToHighlight='''
New estimates from the World Health Organization (WHO) show that the full death toll associated directly or indirectly with the COVID-19 pandemic (described as “excess mortality”) between 1 January 2020 and 31 December 2021 was approximately 14.9 million (range 13.3 million to 16.6 million).  

“These sobering data not only point to the impact of the pandemic but also to the need for all countries to invest in more resilient health systems that can sustain essential health services during crises, including stronger health information systems,” said Dr Tedros Adhanom Ghebreyesus, WHO Director-General. “WHO is committed to working with all countries to strengthen their health information systems to generate better data for better decisions and better outcomes.”

Excess mortality is calculated as the difference between the number of deaths that have occurred and the number that would be expected in the absence of the pandemic based on data from earlier years. 

Excess mortality includes deaths associated with COVID-19 directly (due to the disease) or indirectly (due to the pandemic’s impact on health systems and society). Deaths linked indirectly to COVID-19 are attributable to other health conditions for which people were unable to access prevention and treatment because health systems were overburdened by the pandemic. The estimated number of excess deaths can be influenced also by deaths averted during the pandemic due to lower risks of certain events, like motor-vehicle accidents or occupational injuries. 

Most of the excess deaths (84%) are concentrated in South-East Asia, Europe, and the Americas. Some 68% of excess deaths are concentrated in just 10 countries globally. Middle-income countries account for 81% of the 14.9 million excess deaths (53% in lower-middle-income countries and 28% in upper-middle-income countries) over the 24-month period, with high-income and low-income countries each accounting for 15% and 4%, respectively. 

The estimates for a 24-month period (2020 and 2021) include a breakdown of excess mortality by age and sex. They confirm that the global death toll was higher for men than for women (57% male, 43% female) and higher among older adults. The absolute count of the excess deaths is affected by the population size. The number of excess deaths per 100,000 gives a more objective picture of the pandemic than reported COVID-19 mortality data.

“Measurement of excess mortality is an essential component to understand the impact of the pandemic. Shifts in mortality trends provide decision-makers information to guide policies to reduce mortality and effectively prevent future crises. Because of limited investments in data systems in many countries, the true extent of excess mortality often remains hidden,” said Dr Samira Asma, Assistant Director-General for Data, Analytics and Delivery at WHO. “These new estimates use the best available data and have been produced using a robust methodology and a completely transparent approach.”

“Data is the foundation of our work every day to promote health, keep the world safe, and serve the vulnerable. We know where the data gaps are, and we must collectively intensify our support to countries, so that every country has the capability to track outbreaks in real-time, ensure delivery of essential health services, and safeguard population health,” said Dr Ibrahima Socé Fall, Assistant Director-General for Emergency Response. 

The production of these estimates is a result of a global collaboration supported by the work of the Technical Advisory Group for COVID-19 Mortality Assessment and country consultations. 

This group, convened jointly by the WHO and the United Nations Department of Economic and Social Affairs (UN DESA), consists of many of the world’s leading experts, who developed an innovative methodology to generate comparable mortality estimates even where data are incomplete or unavailable. 

This methodology has been invaluable as many countries still lack capacity for reliable mortality surveillance and therefore do not collect and generate the data needed to calculate excess mortality. Using the publicly available methodology, countries can use their own data to generate or update their own estimates. 

“The United Nations system is working together to deliver an authoritative assessment of the global toll of lives lost from the pandemic. This work is an important part of UN DESA’s ongoing collaboration with WHO and other partners to improve global mortality estimates,” said Mr Liu Zhenmin, United Nations Under-Secretary-General for Economic and Social Affairs. 

Mr Stefan Schweinfest, Director of the Statistics Division of UN DESA, added: “Data deficiencies make it difficult to assess the true scope of a crisis, with serious consequences for people’s lives. The pandemic has been a stark reminder of the need for better coordination of data systems within countries and for increased international support for building better systems, including for the registration of deaths and other vital events.”
'''
        )
    ],
    style={
        'width': '800px',
        'margin': '0 auto'
    }
)


if __name__ == '__main__':
    app.run(debug=True)

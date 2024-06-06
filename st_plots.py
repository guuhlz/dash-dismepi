from pedidos import Pedido
import plotly.express as px
import pandas as pd

def fig_top10_impacto_over(pedido):
    df = pd.melt(pedido.estoque_top10_impacto_over(), 
                 id_vars="Prod_resume",
                 value_vars=["IMPACTO","OVER/DOWN"], 
                 var_name="Measurement", 
                 value_name="Value"
                )

    # Plot
    fig = px.bar(df,
                y="Prod_resume",
                x="Value",
                text="Value",
                barmode='group',
                color='Measurement',  # Color by type of measurement
                labels={"Value": "Value (R$)"},  # Label for y-axis
                category_orders={"Measurement": ["IMPACTO", "OVER/DOWN"]},
                color_discrete_map={'IMPACTO': 'red', 'OVER/DOWN': 'yellow'}
                )

    fig.update_layout(title="Top 10 Impacto e Over",
                        title_x=0.5,
                        title_font=dict(color='white'),
                        xaxis_title="",
                        yaxis_title ="",
                        xaxis_visible=False,
                        plot_bgcolor='rgb(6,31,61)',
                        paper_bgcolor='rgb(6,31,61)',
                        yaxis=dict(position=0),
                        legend=dict(
                            x=0.7,  # Adjust x position (0 to 1)
                            y=0.2,  # Adjust y position (0 to 1)
                            xanchor='left',  # Positioning anchor for x
                            yanchor='top',  # Positioning anchor for y
                            title_text='',  # Remove legend title
                            font=dict(color='white')  # Color of the legend text
                        ),
                        margin=dict(l=0, r=0, t=20, b=50),  # Adjust margins
                        #height=800
                        )

    fig.update_traces(texttemplate="R$ %{text:,.2f}", 
                        textposition="outside",
                        textfont_size=12,
                        textfont_color='white',
                        marker_line_color='black',
                    )
    
    fig.update_yaxes(autorange="reversed",
                        tickfont=dict(color='white'), 
                    )

    return fig

def fig_top10_impacto_down(pedido):
    df = pd.melt(pedido.estoque_top10_impacto_down(), 
                    id_vars="Prod_resume",
                    value_vars=["IMPACTO","OVER/DOWN"],
                    var_name="Measurement",
                    value_name="Value"
                )

    df['Value'] = df['Value'].apply(lambda x: abs(x))

    # Plot
    fig = px.bar(df,
                y="Prod_resume",
                x="Value",
                text="Value",
                barmode='group',
                color='Measurement',  # Color by type of measurement
                labels={"Value": "Value (R$)"},  # Label for y-axis
                category_orders={"Measurement": ["IMPACTO", "OVER/DOWN"]},
                color_discrete_map={'IMPACTO': 'red', 'OVER/DOWN': 'green'}
                )

    fig.update_layout(
        title="Top 10 Impacto e Down",
        title_x=0.5,
        title_font=dict(color='white'),
        xaxis_title="",
        yaxis_title ="",
        xaxis_visible=False,
        plot_bgcolor='rgb(6,31,61)',
        paper_bgcolor='rgb(6,31,61)',
        yaxis=dict(position=0),
        legend=dict(
                            x=0.7,  # Adjust x position (0 to 1)
                            y=0.2,  # Adjust y position (0 to 1)
                            xanchor='left',  # Positioning anchor for x
                            yanchor='top',  # Positioning anchor for y
                            title_text='',  # Remove legend title
                            font=dict(color='white')  # Color of the legend text
                        ),
        margin=dict(l=0, r=0, t=20, b=50),  # Adjust margins
    )

    fig.update_traces(texttemplate="-R$ %{text:,.2f}", 
                    textposition="outside",
                    textfont_size=12,
                    textfont_color='white',
                    marker_line_color='black',
                    )

    fig.update_yaxes(autorange="reversed",
                    tickfont=dict(color='white'), 
                    )



    return fig

def fig_percentual_over_10(pedido):
    df=pedido.estoque_top10_percentual_over()

    fig = px.bar(df,
                y="Prod_resume",
                x="PERCENTUAL OVER/DOWN",
                text="PERCENTUAL OVER/DOWN",
                
    )

    fig.update_layout(
        title="Top 10 Percentual Over",
        title_x=0.5,
        title_font=dict(color='white'),
        xaxis_title="",
        xaxis=dict(
            side='top',  # Move the x-axis to the top
            tickangle=0,  # Angle of the ticks
            title_standoff=0,  # No space between axis and title
            automargin=True  # Automatic margin adjustment
        ),
        yaxis_title ="",
        xaxis_visible=False,
        plot_bgcolor='rgb(6,31,61)',
        paper_bgcolor='rgb(6,31,61)',
        margin=dict(l=0, r=0, t=20, b=150),  # Adjust margins
        

    
    )

    fig.update_traces(texttemplate="%{text:,.2f}%",
                    textposition="outside",
                    textfont_size=12,
                    textfont_color='white',
                    marker_color='yellow',
                    marker_line_color='black')  

    fig.update_yaxes(autorange="reversed",
                    tickfont=dict(color='white'), 
                    )



    return fig


def fig_percentual_down_10(pedido):
    df=pedido.estoque_top10_percentual_down()

    df['PERCENTUAL OVER/DOWN'] = df['PERCENTUAL OVER/DOWN'].apply(lambda x: abs(x))

    fig = px.bar(df,
                y="Prod_resume",
                x="PERCENTUAL OVER/DOWN",
                text="PERCENTUAL OVER/DOWN",
                
    )

    fig.update_layout(
        title="Top 10 Percentual Over",
        title_x=0.5,
        title_font=dict(color='white'),
        xaxis_title="",
        yaxis_title ="",
        xaxis_visible=False,
        plot_bgcolor='rgb(6,31,61)',
        paper_bgcolor='rgb(6,31,61)',
        margin=dict(l=0, r=0, t=20, b=150),  # Adjust margins

    
    )

    fig.update_traces(texttemplate="-%{text:,.2f}%",
                    textposition="inside",
                    textfont_size=12,
                    textfont_color='white',
                    marker_color='green',
                    marker_line_color='black')  

    fig.update_yaxes(autorange="reversed",
                    tickfont=dict(color='white'), 
                    )



    return fig
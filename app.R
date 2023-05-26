# load the required packages
library(shiny)
require(shinydashboard)
library(plotly)
library(dplyr)
library(ggplot2)

supermarket_sales <-read.csv2("./data/supermarket_sales.csv", header = TRUE, sep = ",", dec=".",na.strings =c("","NA"),)

header <- dashboardHeader(title = "Einzelhandelsumsaetze")
sidebar <- dashboardSidebar(
  sidebarMenu(
    menuItem("Dashboard", tabName = "dashboard", icon = icon("dashboard")),
    menuItem("Filter", selectInput("Filiale", label = "Waehlen Sie eine Filiale",
                                   choices = c("Alle",'A', 'B', "C"), selected = 'Alle' ))
  )
)




row1 <- fluidRow(
  box(
  title = "Umsatz pro Filliale"
  ,status = "primary"
  ,solidHeader = TRUE
  ,collapsible = FALSE
  ,plotlyOutput("revenuebySuperMarket", height = "480px")
) ,box(
    title = "Umsatz pro Produkt"
    ,status = "primary"
    ,solidHeader = TRUE
    ,collapsible = FALSE
    ,plotlyOutput("revenuebyProduct", height = "480px")
  ))
row2 <- fluidRow(box(
  title = "Verteilung der Umsätze pro Filiale"
  ,status = "primary"
  ,solidHeader = TRUE
  ,collapsible = FALSE
  ,plotlyOutput("violinPlotSales", height = "480px")
),box(
  title = "Kunden Art"
  ,status = "primary"
  ,solidHeader = TRUE
  ,collapsible = FALSE
  ,plotlyOutput("kuchenMemberArt", height = "480px")
))
body <- dashboardBody(row1, row2)
ui <- dashboardPage(title = 'Einzelhandelsumsaetze', header, sidebar, body, skin='blue')
server <- function(input, output) {
  getData <-function () {
    if(input$Filiale == "Alle"){
      supermarket_sales <- supermarket_sales
    }else{
      supermarket_sales <- supermarket_sales[supermarket_sales$Filiale == input$Filiale,]
    }
    return(supermarket_sales)
  }
  output$revenuebySuperMarket <- renderPlotly({
    supermarket_sales <- getData()
    plot_ly(

      x = supermarket_sales$Datum,

      y=supermarket_sales$Gesamtpreis,

      color=supermarket_sales$Filiale,

      type = "bar"


    )%>% layout(title = "Umsatz pro Filiale", xaxis = list(title = 'Filliale'), yaxis = list(title = 'Umsatz in Euro'), barmode='stack')


  })
  output$revenuebyProduct <- renderPlotly({
    supermarket_sales <- getData()
    plot_ly(

      x = supermarket_sales$Datum,

      y=supermarket_sales$Gesamtpreis,

      color=supermarket_sales$Produktlinie,

      type = "bar"


    )%>% layout(title = "Umsatz pro Produktgruppe", xaxis = list(title = 'Produktgruppe'), yaxis = list(title = 'Umsatz in Euro'), barmode='stack')


  })
  output$violinPlotSales <- renderPlotly({
    supermarket_sales <- getData()
    plot_ly(

      x = supermarket_sales$Filiale,

      y=supermarket_sales$Gesamtpreis,

      type = "violin",
      box = list(visible = T),
      meanline = list(visible = T)


    )%>% layout(title = "Umsatz pro Filiale", xaxis = list(title = 'Filiale'), yaxis = list(title = 'Verteilung der Verkäufe')   )


  })
  output$kuchenMemberArt <- renderPlotly({
    supermarket_sales <- getData()
    plot_ly(
      labels = supermarket_sales$Kundenart,
      values=supermarket_sales$n,
      type = "pie")
  })
}

shinyApp(ui,  server)
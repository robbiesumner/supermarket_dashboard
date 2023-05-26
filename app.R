# load the required packages


library(shiny)
require(shinydashboard)
library(plotly)
library(dplyr)

supermarket_sales <-read.csv2("./data/supermarket_sales.csv", header = TRUE, sep = ",", dec=".",na.strings =c("","NA"),)

header <- dashboardHeader(title = "Einzelhandelsumsätze")
sidebar <- dashboardSidebar(
  sidebarMenu(
    menuItem("Dashboard", tabName = "dashboard", icon = icon("dashboard")),
    menuItem("Filter", selectInput("Filliale", label = "Wählen Sie eine Filiale",
                                   choices = c("Alle",'A', 'B', "C"), selected = 'Alle' ))
  )
)




row1 <- fluidRow(
  box(
  title = "Umsatz pro Filliale"
  ,status = "primary"
  ,solidHeader = TRUE
  ,collapsible = TRUE
  ,plotlyOutput("revenuebyRegion", height = "480px")
) ,2)
row2 <- fluidRow(3,4)
body <- dashboardBody(row1, row2)
ui <- dashboardPage(title = 'Einzelhandelsumsätze', header, sidebar, body, skin='yellow')
server <- function(input, output) {

  output$revenuebyRegion <- renderPlotly({
    plot_ly(

      x = supermarket_sales$Datum,

      y=supermarket_sales$Gesamtpreis,

      color=supermarket_sales$Filiale,

      type = "bar"

    )%>% layout(title = "Umsatz pro Produkt", xaxis = list(title = 'Produkt'), yaxis = list(title = 'Umsatz in Euro'))


  })
}

shinyApp(ui,  server)
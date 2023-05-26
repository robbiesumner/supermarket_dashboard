# load the required packages


library(shiny)
require(shinydashboard)
library(plotly)
library(dplyr)



header <- dashboardHeader(title = "Einzelhandelsumsätze")
sidebar <- dashboardSidebar(
  sidebarMenu(
    menuItem("Dashboard", tabName = "dashboard", icon = icon("dashboard")),
    menuItem("Filter", selectInput("Filliale", label = "Wählen Sie eine Filiale",
                                   choices = c("Alle",'A', 'B', "C"), selected = 'Alle' ))
  )
)

body <- dashboardBody()
ui <- dashboardPage(title = 'Einzelhandelsumsätze', header, sidebar, body, skin='yellow')
server <- function(input, output) { }

shinyApp(ui,  server)
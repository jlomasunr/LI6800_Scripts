library(readxl)
library(ggplot2)
library(dplyr)
library(tidyr)
library(scales)
##############################################################################
# All WHOLE PLANT gas exchange runs
# "~/Documents/Gas_Exchange/2021-10-04-1257_CGC1_12A_rep1.xlsx",
# "~/Documents/Gas_Exchange/2021-10-26-1347_CGC1_t1_wholeplant_complete.xlsx",
# "~/Documents/Gas_Exchange/2021-09-27-1153_CGC-12B_Rep1.xlsx",
# "~/Documents/Gas_Exchange/2021-09-28-1307_CGC_11A_rep1.xlsx",
#"~/Documents/Gas_Exchange/2021-10-27-1423_CAM9_12a_t1_wholeplant.xlsx",
# experiments <- c(
#   "~/Documents/Gas_Exchange/2021-09-29-1451_CAM7_16_rep1.xlsx",
#   "~/Documents/Gas_Exchange/2021-09-30-1513_CAM_9_4_rep1.xlsx",
#   "~/Documents/Gas_Exchange/2021-11-08-1227_CGC1_r1_t1_wholeplant.xlsx"
# )
# # "CGC1 12B Rep1",
# # "CGC1 11A Rep1",
# # "CGC1 12A Rep1",
# # "CGC1 T1",
# series_names <- c(
#   "CAM7 16 Rep1",
#   "CAM 9 4 Rep1",
#   "CGC1 R1 T1"
# )
# group <- c(
#   "CAM7 T2",
#   "CAM9 T2",
#   "CGC1 T1"
# )
# series_colors <- c(
#   "blue",
#   "blue",
#   "blue"
# )
##############################################################################

##############################################################################
# SINGLE LEAF runs 
experiments <- c(
  "~/Documents/Gas_Exchange/2021-11-18-1226_CGC1_T1_R2_plateb_singleleaf.xlsx",
  "~/Documents/Gas_Exchange/2021-11-10-1341_wildtype_singeleaf.xlsx",
  "~/Documents/Gas_Exchange/2021-11-11-1334_wildtype_rep2_singleleaf.xlsx",
  "~/Documents/Gas_Exchange/2021-10-05-CGC_1_11A_rep1-singleleaf.xlsx",
  "~/Documents/Gas_Exchange/2021-10-06-1336_CAM_9_4_rep1_singeleaf.xlsx",
  "~/Documents/Gas_Exchange/2021-10-25-1225_CAM9_t1_singleleaf2.xlsx"

)
#"CAM9 T1",
series_names <- c(
  "CGC1 T1",
  "Wildtype Rep1",
  "Wildtype Rep2",
  "CGC1 T2",
  "CAM9 T2",
  "CAM9 T1"

)

group <- c(
  "CGC1",
  "Wildtype",
  "Wildtype",
  "CGC1",
  "CAM9",
  "CAM9"
)
series_colors <- c(
  "blue",
  "blue",
  "blue",
  "blue",
  "blue",
  "blue"
)
##############################################################################

runs <- data.frame(experiments, series_names, series_colors, group)

combineRuns <- function(df){
  comb <- 0
  for (row in 1:nrow(df)){
    names <- read_excel(df$experiments[row], sheet=1, range="A15:BM15", col_names=FALSE)
    A <- read_excel(df$experiments[row], sheet=1, range="A17:BM304", col_names=FALSE)
    names(A) <- names[1,]
    colnames(A) <- make.unique(names(A))
    A <- A %>% select(time, date, hhmmss, A) 
    A <- A %>% separate(hhmmss, c("hh", "mm", "ss"), ":") 
    A <- A %>% separate(date, c("cal", "hhmmss1"), " ")
    A$cal <- as.numeric(A$cal)
    A$hh <- as.numeric(A$hh)
    A$mm <- as.numeric(A$mm)
    A$ss <- as.numeric(A$ss)
    min <- min(A$cal[1:270])
    A <- A %>% mutate(daynumber = if_else(cal == min, 0, 1)) %>%
               mutate(cum_ss = (hh*60*60) + (mm*60) + (ss) + (daynumber*(24*60*60))) %>%
               mutate(run = df$series_names[row]) %>%
               mutate(group = df$group[row])
    
    A$cum_hh <- A$cum_ss/(60*60)
    #A <- A %>% mutate(cum_hh_cor = ifelse(group == "CAM9", cum_hh -1.05, cum_hh))
    if (typeof(comb) == "double"){
       comb <- A
    } else {
      comb <- rbind(comb, A)
    }
  }
  return(comb)
}

combined <- combineRuns(runs)

ylimits <- c(-5, 7)

ggplot(combined, aes(x=cum_hh, y=A, color=run)) + 
  geom_line() +
  facet_wrap(~group) +
  ylab("A (µmol m-² s-¹)") +
  xlab("Hours of Day") +
  ggtitle("Comparison of Single Leaf Runs") +
  geom_hline(yintercept=0) +
  scale_y_continuous(limits = ylimits) +
  scale_x_continuous(breaks = scales::pretty_breaks(n = 5)) +
  theme(axis.text=element_text(size=12, face = "bold"),
        plot.title = element_text(size=20, face="bold"),
        axis.title = element_text(size=14, face="bold"))

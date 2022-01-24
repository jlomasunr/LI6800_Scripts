library(readxl)
library(ggplot2)
library(dplyr)
library(tidyr)

file_name <- "~/Documents/Gas_Exchange/2021-11-10-1341_wildtype_singeleaf.xlsx"

names <- read_excel(file_name, sheet=1, range="A15:BM15", col_names=FALSE)
A <- read_excel(file_name, sheet=1, range="A17:BM304", col_names=FALSE)
names(A) <- names[1,]

A <- A %>% select(time, date, hhmmss, A) %>%separate(hhmmss, c("hh", "mm", "ss"), ":") %>% separate(date, c("cal", "hhmmss"), " ")
A$cal <- as.numeric(A$cal)
A$hh <- as.numeric(A$hh)
A$mm <- as.numeric(A$mm)
A$ss <- as.numeric(A$ss)
min <- min(A$cal[1:270])
A <- A %>% mutate(daynumber = if_else(cal == min, 0, 1)) %>%
     mutate(cum_ss = (hh*60*60) + (mm*60) + (ss) + (daynumber*(24*60*60)))


ggplot(A, aes(x=cum_ss, y=A)) +
  geom_line() + 
  ylab("A (µmol m-² s-¹)") +
  xlab("Date/time") +
  geom_hline(yintercept=0) +
  theme(axis.text=element_text(size=12, face = "bold"),
        plot.title = element_text(size=20, face="bold"),
        axis.title = element_text(size=14, face="bold")) 

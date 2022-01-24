
library(readxl)
library(ggplot2)
library(dplyr)

# Only works if you resave the excel sheet after clicking "Calculate Sheet" in the formula tab...
file_name <- "~/Documents/Gas_Exchange/2021-12-21-1202_CGC_t1_singleleaf.xlsx"
title <- "CGC1 T1 R2 b 298/02 - Single Leaf Gas Exchange"

names <- read_excel(file_name, sheet=1, range="A15:BM15", col_names=FALSE)
A <- read_excel(file_name, sheet=1, range="A17:BM304", col_names=FALSE)
names(A) <- names[1,]
 #as.Date(A$date, format = "%Y%m%d %h:%m:%s")
A$date_obj <- as.POSIXct(A$time, origin="1970-01-01")
colnames(A) <- make.unique(names(A))

ylimits <- c(-2,8)

findDark <- function(qin){
  returnval = c()
  i <- 1
  prev_qin <- "0"
  for (x in qin){
    if (!is.na(x)){
      if (x < 300) {
        if (prev_qin >= 300) {
          returnval[1] <- i-1
        }
      }
      if (x >= 300) {
        if (prev_qin < 300) {
          returnval[2] <- i-1
        }
      }
    }
    i <- i+1
    prev_qin <- x
    
  }
  return(returnval)
}
xlimits <- findDark(A$Qin)

ggplot(A, aes(x=date_obj, y=A)) + 
  geom_line() + 
  ylab("A (µmol m-² s-¹)") +
  xlab("Date/time") +
  ggtitle(title) +
  geom_hline(yintercept=0) +
  scale_y_continuous(limits = ylimits) +
  theme(axis.text=element_text(size=12, face = "bold"),
        plot.title = element_text(size=20, face="bold"),
        axis.title = element_text(size=14, face="bold")) +
  annotate("rect", xmin = A$date_obj[xlimits[1]], xmax = A$date_obj[xlimits[2]], ymin = ylimits[1], ymax = ylimits[2], alpha = .5)

  

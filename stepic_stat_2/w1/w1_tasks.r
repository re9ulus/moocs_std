# Stepic, statistics 2, week1 tasks

# Task 2, Done
NA_position <- function(x, y) {
  all(is.na(x) == is.na(y))
}

# Task 3, Done
smart_test <- function(df) {
  t <- table(df)
  if (all(t >= 5)) {
    test.result <- chisq.test(t)
    result <- c(test.result$statistic,
                test.result$parameter,
                test.result$p.value)
  } else {
    result <- fisher.test(t)$p.value
  }
  result
}

# smart_test(mtcars[1:20, c("am", "vs")])
# 0.628483

# smart_test(mtcars[,c("am", "vs")])
# 0.3475355 1.0000000 0.5555115 


# Task 4, Done
most_significant <- function(df) {
  p.values <- apply(df, 2, function(x) chisq.test(table(x))$p.value)
  min.p.value <- min(p.values)
  colnames(df)[p.values == min.p.value]
}

# test_data <- read.csv("https://stepic.org/media/attachments/course/524/test_data.csv", stringsAsFactors = F)
# most_significant(test_data)


# Task 5, Done
means <- apply(iris[, 1:4], 2, mean)
iris$important_cases <- as.factor(ifelse((iris[, 1] > means[1]) + (iris[, 2] > means[2]) + (iris[, 3] > means[3]) + (iris[, 4] > means[4]) >= 3, "Yes", "No"))


# Task 6, Done
get_important_cases <- function(df) {
  means <- apply(df, 2, mean)
  important.items <- as.integer(df[, 1] > means[1])
  for(i in 2:length(means)) {
    important.items <- important.items + as.integer(df[, i] > means[i])
  }
  print(important.items)
  df$important_cases <- factor(ifelse((important.items >= (length(means) %/% 2 + 1)), "Yes", "No"), levels=c("Yes", "No"))
  df
}


# Task 7, Done
stat_mode <- function(v) {
  t <- table(v)
  max_val <- max(t)
  as.integer(names(t)[which(t == max_val)])
}


# Task 8, Done
?chisq.test

max_resid <- function(df) {
  t <- chisq.test(table(df))$stdres
  max_val <- max(t)
  
  found = FALSE
  target_row = 0
  target_col = 0
  for(row in 1:nrow(t)) {
    for(col in 1:ncol(t)) {
      if (t[row, col] == max_val) {
        target_row = row
        target_col = col
        found = TRUE
        break
      }    
    }
    if (found) {
      break
    }
  }
  
  c(rownames(t)[target_row], colnames(t)[target_col])
}

# Accurate solution
max_resid <- function(test_data){    
  d <- table(test_data)    
  chi <- chisq.test(d)    
  ind <- which(chi$stdres==max(chi$stdres), arr.ind = T)    
  return(c(row.names(d)[ind[1]],colnames(d)[ind[2]]))    
}

test_data <- read.csv("https://stepic.org/media/attachments/course/524/test_drugs.csv")


# Task 9, Done
library("ggplot2")
ggplot(diamonds, aes(x=color, fill=cut)) +
  geom_bar(position='dodge')

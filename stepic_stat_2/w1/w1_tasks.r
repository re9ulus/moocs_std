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

# Task 6

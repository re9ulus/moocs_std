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


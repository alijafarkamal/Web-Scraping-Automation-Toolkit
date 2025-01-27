library(ggplot2)
library(dplyr)
library(tidyr)
# Load the dataset
data <- read.csv("video-games-sales.csv")
# --- Add Log Normalized Columns ---
data <- data %>%
mutate(
log_total_sales = log(total_sales + 1),
log_na_sales = log(na_sales + 1),
log_jp_sales = log(jp_sales + 1),
log_pal_sales = log(pal_sales + 1),
log_other_sales = log(other_sales + 1)
)
# Print first few rows to verify the added columns
print("Dataset with Log-Normalized Columns:")
print(head(data))
# --- Descriptive Statistics for Sales by Region ---
# 1. Compute mean, median, and standard deviation for sales in each region
region_stats <- data %>%
summarise(
Mean_NA = mean(na_sales, na.rm = TRUE),
Median_NA = median(na_sales, na.rm = TRUE),
SD_NA = sd(na_sales, na.rm = TRUE),
Mean_JP = mean(jp_sales, na.rm = TRUE),
Median_JP = median(jp_sales, na.rm = TRUE),
SD_JP = sd(jp_sales, na.rm = TRUE),
Mean_PAL = mean(pal_sales, na.rm = TRUE),
Median_PAL = median(pal_sales, na.rm = TRUE),
SD_PAL = sd(pal_sales, na.rm = TRUE),
Mean_Other = mean(other_sales, na.rm = TRUE),
Median_Other = median(other_sales, na.rm = TRUE),
SD_Other = sd(other_sales, na.rm = TRUE)
)
print("Descriptive Statistics for Sales by Region:")
print(region_stats)
# --- Descriptive Statistics for Log-Normalized Sales ---
log_region_stats <- data %>%
summarise(
Mean_Log_NA = mean(log_na_sales, na.rm = TRUE),
Median_Log_NA = median(log_na_sales, na.rm = TRUE),
SD_Log_NA = sd(log_na_sales, na.rm = TRUE),
Mean_Log_JP = mean(log_jp_sales, na.rm = TRUE),
Median_Log_JP = median(log_jp_sales, na.rm = TRUE),
SD_Log_JP = sd(log_jp_sales, na.rm = TRUE),
Mean_Log_PAL = mean(log_pal_sales, na.rm = TRUE),
Median_Log_PAL = median(log_pal_sales, na.rm = TRUE),
SD_Log_PAL = sd(log_pal_sales, na.rm = TRUE),
Mean_Log_Other = mean(log_other_sales, na.rm = TRUE),
Median_Log_Other = median(log_other_sales, na.rm = TRUE),
SD_Log_Other = sd(log_other_sales, na.rm = TRUE)
)
print("Descriptive Statistics for Log-Normalized Sales by Region:")
print(log_region_stats)
# --- Range and Quartile Analysis for Critic Scores ---
range_critic <- range(data$critic_score, na.rm = TRUE)
quartiles_critic <- quantile(data$critic_score, na.rm = TRUE)
print("Range of Critic Scores:")
print(range_critic)
print("Quartiles of Critic Scores:")
print(quartiles_critic)
# --- Sales Distribution by Region ---
# 2. Pie Chart: Which region has the most significant game sales?
region_sales <- colSums(data[c("na_sales", "jp_sales", "pal_sales", "other_sales")])
region_df <- data.frame(region = names(region_sales), sales = region_sales)
ggplot(region_df, aes(x = "", y = sales, fill = region)) +
geom_bar(stat = "identity", width = 1) +
coord_polar("y") +
labs(title = "Regional Sales Distribution", y = "Sales", fill = "Region")
# 3. Histogram: Distribution of Total Sales by Platform and Genre
ggplot(data, aes(x = log_total_sales, fill = genre)) +
geom_histogram(binwidth = 2, alpha = 0.7, position = "identity") +
facet_wrap(~console) +
labs(title = "Distribution of Total Sales by Platform and Genre", x = "Total Sales", y
= "Frequency")
# 4. Histogram: Log-Total Sales
ggplot(data, aes(x = log_total_sales)) +
geom_histogram(binwidth = 0.1, fill = "blue", color = "black", alpha = 0.7) +
labs(title = "Distribution of Log-Total Sales", x = "Log-Total Sales", y =
"Frequency") +
theme_minimal()
# 5. Bar Plot: Publishers with Most Releases
publisher_stats <- data %>%
group_by(publisher) %>%
summarise(releases = n(), total_sales = sum(total_sales)) %>%
arrange(desc(releases)) %>%
head(10)
ggplot(publisher_stats, aes(x = reorder(publisher, -releases), y = releases, fill =
total_sales)) +
geom_bar(stat = "identity") +
labs(title = "Top 10 Publishers by Releases", x = "Publisher", y = "Number of
Releases") +
theme(axis.text.x = element_text(angle = 45, hjust = 1))
# 6. Box Plot: Sales Variations by Region (Identify Outliers)
melted_sales <- data %>%
select(na_sales, jp_sales, pal_sales, other_sales) %>%
pivot_longer(everything(), names_to = "Region", values_to = "Sales")
ggplot(melted_sales, aes(x = Region, y = Sales, fill = Region)) +
geom_boxplot(outlier.colour = "red", outlier.shape = 16) +
labs(title = "Sales Variations by Region", x = "Region", y = "Sales") +
theme_minimal()
# 7. Box Plot: Log-Normalized Sales Variations by Region
log_melted_sales <- data %>%
select(log_na_sales, log_jp_sales, log_pal_sales, log_other_sales) %>%
pivot_longer(everything(), names_to = "Region", values_to = "Log_Sales")
ggplot(log_melted_sales, aes(x = Region, y = Log_Sales, fill = Region)) +
geom_boxplot(outlier.colour = "red", outlier.shape = 16) +
labs(title = "Log-Normalized Sales Variations by Region", x = "Region", y =
"Log-Sales") +
theme_minimal()
# --- Graph for Critic Score Distribution ---
# 8. Histogram: Distribution of Critic Scores
ggplot(data, aes(x = critic_score)) +
geom_histogram(bins = 20, fill = "skyblue", color = "black", alpha = 0.7) +
labs(title = "Distribution of Critic Scores", x = "Critic Score", y = "Frequency") +
theme_minimal()
# --- Boxplot: Critic Score Distribution and Outliers with Values ---
# Calculate outliers using the boxplot stats
outliers_critic <- boxplot.stats(data$critic_score)$out
# Create a data frame for outliers
outliers_df <- data.frame(critic_score = outliers_critic)
# Boxplot with outlier labels
ggplot(data, aes(x = "", y = critic_score)) +
geom_boxplot(outlier.colour = "red", outlier.shape = 16) +
geom_text(data = outliers_df, aes(x = 1, y = critic_score, label = critic_score),
color = "black", size = 3, vjust = -0.5) + # Adjust text placement
labs(title = "Critic Score Distribution with Outliers", y = "Critic Score") +
theme_minimal()
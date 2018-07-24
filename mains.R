i <- 2000
j <- 1
while (i < 2016){
  while (j < 13){
    print(gsub(" ", "", paste(i,".",j), fixed = TRUE))
    j <- j + 1
  }
  i <- i + 1
  j <- 1
}



  

paste(char(i),".",char(j))


# 300, 3-標準正規乱数
x <- matrix(rnorm(900), 300, 3)

# しゅ
pr <- prcomp(scale(x))

# k-means
cl <- kmeans(x, 3)$cl

x11 <- pr$x[cl==1,1]

# step1～環境設定
tab <- '\\'
ub <- '_'
date <- '161111'
time <- '1617'
path <- 'C:\\Users\\1500570\\Desktop\\pleiades\\workspace\\Jinryu_Kaiseki\\'
filename <- 'formap.csv'
filepath <- paste(path, date, ub, time, tab, date, ub, time, ub, filename, sep="")

data <- read.csv(filepath, header=T, sep=",")
head(data)

# step2～プロッターの作成
# 速度別
data1 <- subset(data, 0 < velocity | velocity < 0.7 | velocity == 0.7, c(x, y))
data2 <- subset(data, 0.7 < velocity | velocity < 1.4 | velocity == 1.4, c(x, y))
data3 <- subset(data, 1.4 < velocity, c(x, y))

# グリッド色分け
data1 <- subset(data, grid_x %% 2 == 0 & grid_y %% 2 == 0, c(x, y))
data2 <- subset(data, grid_x %% 2 == 1 & grid_y %% 2 == 0, c(x, y))
data3 <- subset(data, grid_x %% 2 == 0 & grid_y %% 2 == 1, c(x, y))
data4 <- subset(data, grid_x %% 2 == 1 & grid_y %% 2 == 1, c(x, y))

# 東西南北別
data1 <- subset(data, direction > -45 & direction < 45, c(x, y))
data2 <- subset(data, direction > -180 & direction < -135 & direction , c(x, y))
data22 <- subset(data, direction > 135 & direction < 180, c(x, y))
data3 <- subset(data, direction > -135 & direction < -45, c(x, y))
data4 <- subset(data, direction > 45 & direction < 135, c(x, y))

# 境界線テスト
data1 <- subset(data, x >= 37000 & x < 38000 & y >= 25000 & y < 35000, c(x, y))
data2 <- subset(data, x >= 58000 & x < 62000 & y >= 30000 & y < 31000, c(x, y))
data3 <- subset(data, x >= 69000 & x < 74000 & y >= 27500 & y < 28500, c(x, y))
data4 <- subset(data, x >= 100500 & x < 101500 & y >= 40000 & y < 54000, c(x, y))
data6 <- subset(data, x >= 74100 & x < 75100 &  y >= 15000 & y < 30000, c(x,y))
data7 <- subset(data, x >= 56000 & x < 57000 & y >= 18000 & y < 26000, c(x, y))
data8 <- subset(data, x >= 90000 & x < 110000 & y >= 53000 & y < 54000, c(x,y))
data9 <- subset(data, x >= 90000 & x < 110000 & y >= 38000 & y < 39000, c(x,y))
data10 <- subset(data,x >= 55000 & x < 60000 & y >= 18000 & y < 19000, c(x,y))
data11 <- subset(data,x >= 66000 & x < 74000 & y >= 20000 & y < 21000, c(x,y))
dataa <- subset(data, x >= 0, c(x,y))

# step3～プロット
# test1
png("plot.png",width=1000,height = 1000)
plot(data2, xlim = c(-6000, 20000), col=rgb(0, 1, 0, alpha=0.01), pch=19, cex=2)
par(new=T)
plot(data1, xlim = c(-6000, 20000), col=rgb(0, 0, 1, alpha=0.01), pch=19, cex=2)
par(new=T)
plot(data3, xlim = c(-6000, 20000), col=rgb(1, 0, 0, alpha=0.01), pch=19, cex=2)
dev.off()
points(data, col=rgb(1, 0, 0), pch=19, cex=2)

# test2
png("plot3.png",width=1200,height = 700)
plot(data4, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(1, 0, 0, alpha=0.1), pch=0.1, cex=0.01)
par(new=T)
plot(data3, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(0, 1, 0, alpha=0.1), pch=0.1, cex=0.01)
par(new=T)
plot(data2, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(0, 1, 1, alpha=0.1), pch=0.1, cex=0.01)
par(new=T)
plot(data1, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(0, 0, 1, alpha=0.1), pch=0.1, cex=0.01)
par(new=T)
dev.off()

# east
png("161111_1617_plot_east.png", width=1200,height = 700)
plot(data1, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(1, 0, 0, alpha=0.01), pch=0.01, cex=0.001)
par(new=T)
dev.off()

# west
png("161111_1617_plot_west.png", width=1200,height = 700)
plot(data2, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(1, 0, 0, alpha=0.01), pch=0.01, cex=0.001)
par(new=T)
plot(data22, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(1, 0, 0, alpha=0.01), pch=0.01, cex=0.001)
par(new=T)
dev.off()

# south
png("161111_1617_plot_south.png", width=1200, height = 700)
plot(data3, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(1, 0, 0, alpha=0.01), pch=0.01, cex=0.001)
par(new=T)
dev.off()

# norht
png("161111_1617_plot_north.png",width=1200,height = 700)
plot(data4, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(1, 0, 0, alpha=0.01), pch=0.01, cex=0.001)
par(new=T)
dev.off()

# 境界線テスト

png("plot11.png",width=1200,height = 700)
plot(dataa, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(0.5, 0.5, 0.5, alpha=0.01), pch=0.01, cex=0.001)
par(new=T)
plot(data1, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(1, 0, 0, alpha=0.1), pch=0.1, cex=0.1)
par(new=T)
plot(data2, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(0, 1, 0, alpha=0.1), pch=0.1, cex=0.1)
par(new=T)
plot(data3, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(0, 0, 1, alpha=0.1), pch=0.1, cex=0.1)
par(new=T)
plot(data4, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(1, 1, 0, alpha=0.1), pch=0.1, cex=0.1)
par(new=T)
plot(data6, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(0, 1, 1, alpha=0.1), pch=0.1, cex=0.1)
par(new=T)
plot(data7, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(1, 0, 1, alpha=0.1), pch=0.1, cex=0.1)
par(new=T)
plot(data8, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(0.7, 0.3, 0, alpha=0.1), pch=0.1, cex=0.1)
par(new=T)
plot(data9, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(0, 0.7, 0.3, alpha=0.1), pch=0.1, cex=0.1)
par(new=T)
plot(data10, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(0.2, 0.5, 0.3, alpha=0.1), pch=0.1, cex=0.1)
par(new=T)
plot(data11, xlim = c(0, 120000), ylim = c(0, 70000), col=rgb(0.4, 0.3, 0.3, alpha=0.1), pch=0.1, cex=0.1)
par(new=T)
dev.off()

points(data, col=rgb(1, 0, 0), pch=19, cex=2)

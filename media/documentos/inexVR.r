library(xlsx)
datos<-read.xlsx("avaluos2017.xlsx", 1)
head(datos)

x<-dim(datos) 
x
x[1]


vector<-c(1,3,5,7,9,12,15,18,30,35)
vector2<-c(1:10)
plot(vector, type = "s", col="blue")
?plot
lines(vector2, type = "s", col="red")

barplot(vector)

hist(vector)
pie(vector)


provincia<-factor(c("Huelva","Huelva","Ja�n","Sevilla","Almer�a"),
                  levels=c("Huelva","C�diz","M�laga","Granada","Almer�a","Ja�n","C�rdoba","Sevilla"))
provincia


head(datos)
factorial(5)
choose(5,5)


x= c(1,2,3,4,5,6,7)
x
x=pi * 2
x
x=(pi^2)/2
x


ls()

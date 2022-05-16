--Dataset Source: https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease

CREATE TABLE HeartDiseaseData
(PercentageSmokers decimal(18,2),
PercentageDrinkers decimal(18,2),
PercentageStroke decimal(18,2),
PercentageBadMentalHealth decimal(18,2),
PercentageBadPhysicalHealth decimal(18,2),
PercentageDifficultyWalking decimal(18,2),
PercentagePhysicalActivity decimal(18,2),
PercentageAsthma decimal(18,2),
PercentageKidneyDisease decimal(18,2),
PercentageSkinCancer decimal(18,2),
PercentageAbove65 decimal(18,2),
PercentagePoorGenHealth decimal(18,2)
)

select *
from PortfolioProject..heart_2020_cleaned$

select count(HeartDisease)
from PortfolioProject..heart_2020_cleaned$
where HeartDisease = 'Yes'
--27373

select count(Smoking)
from PortfolioProject..heart_2020_cleaned$
where Smoking = 'Yes' and HeartDisease = 'Yes'
--16037

select count(AlcoholDrinking)
from PortfolioProject..heart_2020_cleaned$
where AlcoholDrinking = 'Yes' and HeartDisease = 'Yes'
--1141

select count(Stroke)
from PortfolioProject..heart_2020_cleaned$
where Stroke = 'Yes' and HeartDisease = 'Yes'
--4389

select count(MentalHealth)
from PortfolioProject..heart_2020_cleaned$
where MentalHealth > 15 and HeartDisease = 'Yes'
--3184

select count(PhysicalHealth)
from PortfolioProject..heart_2020_cleaned$
where PhysicalHealth > 15 and HeartDisease = 'Yes'
--5946

select count(DiffWalking)
from PortfolioProject..heart_2020_cleaned$
where DiffWalking ='Yes' and HeartDisease = 'Yes'
--10028

select count(PhysicalActivity)
from PortfolioProject..heart_2020_cleaned$
where PhysicalActivity ='Yes' and HeartDisease = 'Yes'
--17489

select count(Asthma)
from PortfolioProject..heart_2020_cleaned$
where Asthma ='Yes' and HeartDisease = 'Yes'
--4933

select count(KidneyDisease)
from PortfolioProject..heart_2020_cleaned$
where KidneyDisease ='Yes' and HeartDisease = 'Yes'
--3455

select count(SkinCancer)
from PortfolioProject..heart_2020_cleaned$
where SkinCancer ='Yes' and HeartDisease = 'Yes'
--4980

select count(AgeCategory)
from PortfolioProject..heart_2020_cleaned$
where (AgeCategory = '65-69' or AgeCategory = '70-74' or AgeCategory = '75-79' or AgeCategory='80 or older') and HeartDisease='yes'
--18446

select count(GenHealth)
from PortfolioProject..heart_2020_cleaned$
where GenHealth = 'Poor' and HeartDisease='yes'
--3850

Insert Into HeartDiseaseData Values
( cast(16037 as float)/cast(27373 as float)*100, cast(1141 as float)/cast(27373 as float)*100, cast(4389 as float)/cast(27373 as float)*100, cast(3184 as float)/cast(27373 as float)*100, cast(5946 as float)/cast(27373 as float)*100, cast(10028 as float)/cast(27373 as float)*100, cast(17489 as float)/cast(27373 as float)*100, cast(4933 as float)/cast(27373 as float)*100, cast(3455 as float)/cast(27373 as float)*100, cast(4980 as float)/cast(27373 as float)*100, cast(18446 as float)/cast(27373 as float)*100, cast(3850 as float)/cast(27373 as float)*100)


select *
from HeartDiseaseData

--nearly 60% of the people in the Dataset with heart disease smoke cigarettes, and almost 70% are above the age of 65

--Dataset Source: https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-outcomes-and?select=aac_shelter_cat_outcome_eng.csv
--This Dataset contains information about cats from the Austin Animal Shelter in the US and their outcomes
--The Austin Animal Shelter is the largest no-kill shelter in the US and provides daily data about their animals
--My goal is to investigate the most common types of cats that get adopted

--Viewing all data:
SELECT *
FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes
ORDER BY age_upon_outcome

--Observing outcomes of cats by gender
SELECT outcome_type, sex, (COUNT(sex)*100/ 
	(SELECT COUNT(*) 
	FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes 
	WHERE outcome_type LIKE 'Ado%')) as Percentage_of_cats
FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes 
WHERE outcome_type LIKE 'Ado%'
GROUP BY outcome_type, sex
ORDER BY outcome_type
--51% of adopted cats are female and 49% are male

--Observing outcomes of cats by spay/neuter status
SELECT outcome_type, [Spay/Neuter], (COUNT([Spay/Neuter])*100/ 
	(SELECT COUNT(*) 
	FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes 
	WHERE outcome_type LIKE 'Ado%')) as Percentage_of_cats
FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes
WHERE outcome_type LIKE 'Ado%'
GROUP BY outcome_type, [Spay/Neuter]
ORDER BY outcome_type, [Spay/Neuter]
--94% of adopted cats are spayed or neutered although it is unclear whether that occurs before or after adoption


--Observing the color cat that is most likely to be adopted:
SELECT color, COUNT(color)*100/
	(SELECT COUNT(*) 
	FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes 
	WHERE outcome_type LIKE 'Ado%') AS Percentage_of_cats
FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes
WHERE outcome_type LIKE 'Ado%'
GROUP BY color
ORDER BY Percentage_of_cats DESC 
--The most common color cat that is adopted is brown at 16% of all adopted cats

--Observing whether Cats or Kittens are more likely to be adopted
SELECT [Cat/Kitten (outcome)], COUNT([Cat/Kitten (outcome)])*100/
	(SELECT COUNT(*) 
	FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes 
	WHERE outcome_type LIKE 'Ado%') AS Percentage_adopted
FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes
WHERE outcome_type LIKE 'Ado%'
GROUP BY [Cat/Kitten (outcome)]
ORDER BY Percentage_adopted DESC 
--68% of all adopted cats are kittens

--Observing the adoption rates at different age groups
SELECT age_group, COUNT(age_group)*100/
	(SELECT COUNT(*) 
	FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes 
	WHERE outcome_type LIKE 'Ado%') AS Percentage_adopted
FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes
WHERE outcome_type LIKE 'Ado%'
GROUP BY age_group
ORDER BY Percentage_adopted DESC 
--87% of all adopted cats are between the ages of 0-2.2 years old
--4% are between 2.2-4.4
--2% are between 6.6-8.8

--Observing the adoption rates at different days of the week
SELECT outcome_weekday, COUNT(outcome_weekday)*100/
	(SELECT COUNT(*) 
	FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes 
	WHERE outcome_type LIKE 'Ado%') AS Percentage_adopted
FROM ShelterCatOutcomeProject..aac_shelter_cat_outcomes
WHERE outcome_type LIKE 'Ado%'
GROUP BY outcome_weekday
ORDER BY Percentage_adopted DESC 
--Cats are most likely to be adopted on Saturdays or Sundays








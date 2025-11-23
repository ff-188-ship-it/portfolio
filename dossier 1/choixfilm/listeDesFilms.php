<?php
require("connect.php");

$connexion = mysqli_connect(SERVEUR, LOGIN, PASSE);
if (!$connexion) {
    echo "Connexion à " . SERVEUR . " impossible\n";
    exit;
}

if (!mysqli_select_db($connexion, BASE)) {
    echo "Accès à la base " . BASE . " impossible\n";
    exit;
}

// Définir le charset à utf8
mysqli_set_charset($connexion, "utf8");

// Requêtes SQL
$resultats_films = mysqli_query($connexion, "SELECT NumFilm, Titre, I.nom, I.prenom
    FROM MI0A401T_Films AS F
    LEFT JOIN MI0A401T_Individus AS I ON (F.NumInd=I.NumInd)");

$result_filmsdrame = mysqli_query($connexion, "SELECT NumFilm, Titre, I.nom, I.prenom
    FROM MI0A401T_Films AS F
    LEFT JOIN MI0A401T_Individus AS I ON (F.NumInd=I.NumInd)
    WHERE UPPER(F.Genre) = 'DRAME'");

$result_acteurs = mysqli_query($connexion, "SELECT A.NumInd, I.nom, I.prenom, COUNT(A.NumInd) AS nbfilm
    FROM MI0A401T_Acteurs AS A
    INNER JOIN MI0A401T_Individus AS I ON (I.NumInd=A.NumInd)
    LEFT JOIN MI0A401T_Films AS F ON (F.NumFilm=A.NumFilm)
    GROUP BY A.NumInd");

// Vérification des erreurs de requêtes
$error = "";
if (!$resultats_films) {
    $error = mysqli_error($connexion);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Liste des films</title>
    <link rel="stylesheet" href="style/style.css"/>
</head>
<body>
    <h1>Cinémathèque ...</h1>
    <h2>Films</h2>
    
    <?php
    if ($error != "") {
        echo "<p>Erreurs : $error</p>\n";
    } else {
        while ($film = mysqli_fetch_array($resultats_films)) {
            echo "<p>" . $film["NumFilm"] . ". " . $film["Titre"] . " de " . $film["prenom"] . " " . $film["nom"] . "</p>\n";
        }
    }
    ?>

    <h2>Films du genre Drame</h2>
    <?php
    if ($error != "") {
        echo "<p>Erreurs : $error</p>\n";
    } else {
        echo "<table border='1'>";
        echo "<tr><th>NumFilm</th><th>Titre</th><th>Prénom</th><th>Nom</th></tr>";
        while ($film = mysqli_fetch_array($result_filmsdrame)) {
            echo "<tr>";
            echo "<td>" . $film["NumFilm"] . "</td>";
            echo "<td>" . $film["Titre"] . "</td>";
            echo "<td>" . $film["prenom"] . "</td>";
            echo "<td>" . $film["nom"] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    }
    ?>

    <h2>Acteurs</h2>
    <?php
    if ($error != "") {
        echo "<p>Erreurs : $error</p>\n";
    } else {
        echo "<table border='1'>";
        echo "<tr><th>NumInd</th><th>Nom</th><th>Prénom</th><th>Nombre de films</th></tr>";
        while ($acteur = mysqli_fetch_array($result_acteurs)) {
            echo "<tr>";
            echo "<td>" . $acteur["NumInd"] . "</td>";
            echo "<td>" . $acteur["nom"] . "</td>";
            echo "<td>" . $acteur["prenom"] . "</td>";
            echo "<td>" . $acteur["nbfilm"] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    }
    ?>

</body>
</html>

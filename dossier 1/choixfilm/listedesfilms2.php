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

$genre= $_GET['genre'];
$error = "";
if (!$genre) {
    $error = mysqli_error($connexion);
}

$result_genre = mysqli_query($connexion, "SELECT Titre, NumFilm, Genre FROM MI0A401T_Films
WHERE LOWER(Genre) = LOWER('$genre')
ORDER BY NumFilm ;");


?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8" />
    <title>Liste des films </title>
</head>
<body>
<h1>Films du genre : <?= htmlspecialchars($genre) ?></h1>
   <?php
   if ($error != "") {
    echo "<p style='color:red;'>Erreur : $error</p>\n";
}  else {
    echo "<ul>";
    while ($film = mysqli_fetch_array($result_genre)) {
        echo "<li>".$film['NumFilm']. "-" . $film['Titre']. "</li>";
    }
    echo "</ul>";
}

    ?>

    <footer><a href="ChoixFilms.html">retour au formulaire </a></footer>
</body>
</html>

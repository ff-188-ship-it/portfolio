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

// Requête SQL pour récupérer les genres distincts
$result = mysqli_query($connexion, "DESCRIBE MI0A401T_Films");

if (!$result) {
    $error = mysqli_error($connexion);
    echo "Erreur dans la requête : $error";
    exit;
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>CHOIX FILMS</title>
</head>
<body>

    <h1>Cinémathèque...</h1>
    <p>Ce formulaire vous permet de chercher les films <strong>par leur genre</strong></p>

    <form action="listedesfilms2.php" method="get">
        <label for="genre">Quel genre ?</label>
        <select name="genre">
            <?php
            while ($film = mysqli_fetch_array($result)) {
                $genre = htmlspecialchars($film['Genre']); // Protection contre injection HTML
                echo "<option value=\"$genre\">$genre</option>";
            }
            ?>
        </select>
        <br><br>
        <input type="submit" value="Rechercher">
    </form>

    <footer>
        Réalisé par ...
    </footer>

</body>
</html>

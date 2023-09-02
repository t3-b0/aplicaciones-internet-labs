<!DOCTYPE html>
<html>
<head>
    <title>Aplicaciones de Internet</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
</head>
<body>
    <div class="container-fluid">
        <?php
            echo "<h1>Aplicaciones de Internet</h1>";
        
            if (($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['nombre']) && isset($_POST['apellido']))) {
                $nombre = $_POST['nombre'];
                $apellido = $_POST['apellido'];
                $name = $nombre . ' ' . $apellido;
                if(empty($name) or empty($apellido)){
                    echo "faltan datos";
                }else{
                    $conn = mysqli_connect('db', 'root', 'test', 'dbname');

                    if (!$conn) {
                        die("Error de conexión: " . mysqli_connect_error());
                    }
    
                    $query_id = 'SELECT MAX(id) AS id FROM Person';
                    $result = mysqli_query($conn, $query_id);
    
                    if (!$result) {
                        die("Error en la consulta: " . mysqli_error($conn));
                    }
    
                    $row = mysqli_fetch_assoc($result);
                    $id = $row['id'] + 1;
    
                    $query = "INSERT INTO Person (id, name) VALUES ($id, '$name')";
                    if (mysqli_query($conn, $query)) {
                        echo "Registro exitoso.";
                    } else {
                        echo "Error en la inserción: " . mysqli_error($conn);
                    }
                    mysqli_close($conn);
                }
                
            }

            $conn = mysqli_connect('db', 'root', 'test', 'dbname');

            if (!$conn) {
                die("Error de conexión: " . mysqli_connect_error());
            }

            $query = 'SELECT * FROM Person';
            $result = mysqli_query($conn, $query);

            if (!$result) {
                die("Error en la consulta: " . mysqli_error($conn));
            }

            echo '<table class="table table-striped">';
            echo '<thead><tr><th></th><th>id</th><th>name</th></tr></thead>';
            while ($row = mysqli_fetch_assoc($result)) {
                echo '<tr>';
                echo '<td><a href="#"><span class="glyphicon glyphicon-search"></span></a></td>';
                echo '<td>' . $row['id'] . '</td>';
                echo '<td>' . $row['name'] . '</td>';
                echo '</tr>';
            }
            echo '</table>';
            mysqli_close($conn);
            
        ?>
        <form method="POST" action="index.php">
            <div class="form-group">
                <label for="nombre">Nombre:</label>
                <input type="text" class="form-control" id="nombre" name="nombre" required>
            </div>
            <div class="form-group">
                <label for="apellido">Apellido:</label>
                <input type="text" class="form-control" id="apellido" name="apellido" required>
            </div>
            <button type="submit" class="btn btn-primary">Registrar</button>
        </form>
        <div id="dbtest">
            <?php
                
            ?>
        </div>
    </div>
</body>
</html>
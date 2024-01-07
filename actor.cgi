use strict;
use warnings;
use DBI;

my $servername = "localhost";
my $username = "root";
my $password = "contrasena";
my $database = "movies";

my $dbh = DBI->connect("DBI:mysql:database=$database;host=$servername", $username, $password, { PrintError => 0, RaiseError => 1 });

if (!$dbh) {
    die "Conexión fallida: " . DBI::errstr;
}

my $id_actor = 5;
my $sql = "SELECT name_actor FROM actor WHERE id_actor = ?";
my $sth = $dbh->prepare($sql);

$sth->execute($id_actor);

if ($sth->rows > 0) {
    my $row = $sth->fetchrow_hashref();
    print "Nombre del actor con idActor $id_actor: " . "<br>" . $row->{name_actor} . "\n";
} else {
    print "No se encontró ningún actor con idActor = $id_actor\n";
}

$sth->finish();
$dbh->disconnect();

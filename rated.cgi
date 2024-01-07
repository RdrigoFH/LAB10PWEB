#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;

my $cgi = CGI->new;

# Database Connection Parameters
my $servername = "localhost";
my $username = "root";
my $password = "contrasena";
my $database = "movies";

my $dbh = DBI->connect("DBI:mysql:database=$database;host=$servername", $username, $password, { PrintError => 0, RaiseError => 1 });

if (!$dbh) {
    print $cgi->header(-type => 'text/html', -status => '500 Internal Server Error');
    die "Conexión fallida: " . DBI::errstr;
}

my $rate = 7;
my $votes = 5000;
my $sql = "SELECT movie_name FROM movies WHERE rated > ? AND votes > ?";
my $sth = $dbh->prepare($sql);

$sth->execute($rate, $votes);

print $cgi->header(-type => 'text/html');

if ($sth->rows > 0) {
    while (my $row = $sth->fetchrow_hashref()) {
        print "Peliculas con más de 5000 votos y valoración mayor a 7: " . $row->{movie_name} . "<br>";
    }
} else {
    print "No se encontraron películas\n";
}
$sth->finish();
$dbh->disconnect();

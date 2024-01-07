#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;

# CGI Initialization
my $cgi = CGI->new;

my $servername = "localhost";
my $username = "root";
my $password = "contrasena";
my $database = "movies";

my $dbh = DBI->connect("DBI:mysql:database=$database;host=$servername", $username, $password, { PrintError => 0, RaiseError => 1 });

if (!$dbh) {
    print $cgi->header(-type => 'text/html', -status => '500 Internal Server Error');
    die "Conexión fallida: " . DBI::errstr;
}

my $year = 1985;
my $sql = "SELECT movie_name FROM movies WHERE movie_year = ?";
my $sth = $dbh->prepare($sql);

$sth->execute($year);

print $cgi->header(-type => 'text/html');

if ($sth->rows > 0) {
    my $row = $sth->fetchrow_hashref();
    print "Peliculas que coinciden con el año $year: " . "<br>" . $row->{movie_name} . "\n";
} else {
    print "No se encontró la película del año $year\n";
}

$sth->finish();
$dbh->disconnect();

#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;

my $cgi = CGI->new;

require 'connect.pl';

my $servername = "localhost";
my $username = "root";
my $password = "Amomifamilia3";
my $database = "movies";

my $dbh = DBI->connect("DBI:mysql:database=$database;host=$servername", $username, $password, { PrintError => 0, RaiseError => 1 });

if (!$dbh) {
    print $cgi->header(-type => 'text/html', -status => '500 Internal Server Error');
    die "Conexión fallida: " . DBI::errstr;
}

if ($cgi->request_method eq 'POST') {
    my $year = $cgi->param('year');

    my $sql = "SELECT movie_name FROM movies WHERE movie_year = ?";
    my $sth = $dbh->prepare($sql);

    $sth->execute($year);

    print $cgi->header(-type => 'text/html');

    print "<h2>Películas del año $year:</h2>";

    if ($sth->rows > 0) {
        while (my $row = $sth->fetchrow_hashref()) {
            print $row->{movie_name} . "<br>";
        }
    } else {
        print "No se encontraron películas para el año $year.";
    }

    $sth->finish();
}

$conn->disconnect();

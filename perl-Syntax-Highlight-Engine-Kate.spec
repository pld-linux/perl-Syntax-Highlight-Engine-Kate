#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Syntax
%define		pnam	Highlight-Engine-Kate
%include	/usr/lib/rpm/macros.perl
Summary:	Syntax::Highlight::Engine::Kate - a port to Perl of the syntax highlight engine of the Kate texteditor
Summary(pl.UTF-8):	Syntax::Highlight::Engine::Kate - perlowy port silnika podświetlania składni z edytora Kate
Name:		perl-Syntax-Highlight-Engine-Kate
Version:	0.14
Release:	1
# same as perl 5.8.3+
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Syntax/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	10df4c2d1df9a99f04ec7b03f807e8c2
URL:		http://search.cpan.org/dist/Syntax-Highlight-Engine-Kate/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.59
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Term-ANSIColor
BuildRequires:	perl-Test-Differences >= 0.61
BuildRequires:	perl-Test-Simple >= 1.00
BuildRequires:	perl-Test-Warn >= 0.30
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Syntax::Highlight::Engine::Kate is a port to Perl of the syntax
highlight engine of the Kate text editor.

The language XML files of Kate have been rewritten to Perl modules
using a script. These modules function as plugins to this module.

%description -l pl.UTF-8
Syntax::Highlight::Engine::Kate to perlowy port silnika podświetlania
składni edytora Kate.

Pliki języków edytora Kate w formacie XML zostały przepisane do
modułów Perla przy użyciu skryptu. Funkcjonują jako wtyczki dla tego
modułu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Syntax
%dir %{perl_vendorlib}/Syntax/Highlight
%dir %{perl_vendorlib}/Syntax/Highlight/Engine
%{perl_vendorlib}/Syntax/Highlight/Engine/Kate.pm
%{perl_vendorlib}/Syntax/Highlight/Engine/Kate
%{_mandir}/man3/Syntax::Highlight::Engine::Kate*.3pm*
%{_examplesdir}/%{name}-%{version}

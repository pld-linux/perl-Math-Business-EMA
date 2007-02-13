#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Business-EMA
Summary:	Math::Business::EMA - Perl extension for calculating EMAs
Summary(pl.UTF-8):	Math::Business::EMA - rozszerzenie Perla do obliczania EMA
Name:		perl-Math-Business-EMA
Version:	1.08
Release:	1
License:	unknown
Vendor:		Jettero Heller <jettero@cpan.org>
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5b723fd740392d9d5f0b90042e26b802
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Math-Business-SMA >= 0.99
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Business::EMA - Perl extension for calculating EMAs.

%description -l pl.UTF-8
Math::Business::EMA - rozszerzenie Perla do obliczania EMA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Math/Business/EMA.pm
%{_mandir}/man3/*

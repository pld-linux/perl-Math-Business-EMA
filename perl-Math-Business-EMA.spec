#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Business-EMA
Summary:	Math::Business::EMA - Perl extension for calculating EMAs
Summary(pl):	Math::Business::EMA - rozszerzenie Perla do obliczania EMA
Name:		perl-Math-Business-EMA
Version:	1.06
Release:	1
License:	unknown
Vendor:		Jettero Heller <jettero@cpan.org>
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Math-Business-SMA >= 0.99
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Business::EMA - Perl extension for calculating EMAs.

%description -l pl
Math::Business::EMA - rozszerzenie Perla do obliczania EMA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Math/Business/EMA.pm
%{_mandir}/man3/*

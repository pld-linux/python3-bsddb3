%define		pname	bsddb3
Summary:	Python interface for BerkeleyDB
Summary(pl.UTF-8):	Interfejs Pythona do BerkeleyDB
Name:		python3-bsddb3
Version:	4.7.5
Release:	1
License:	BSD-like w/o adv. clause
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/b/bsddb3/bsddb3-%{version}.tar.gz
# Source0-md5:	8f0773f5de160c39263f5af9ead1d0dc
URL:		http://www.argo.es/~jcea/programacion/pybsddb.htm
BuildRequires:	db-devel >= 4.1.25
BuildRequires:  python3
BuildRequires:	python3-devel
BuildRequires:	rpm-build-macros >= 1.507
%pyrequires_eq	python3-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a nearly complete wrapping of the Oracle C API
for the Database Environment, Database, Cursor, and Transaction
objects, and each of these is exposed as a Python Type in the
bsddb3.db module. The databse objects can use various access methods:
btree, hash, recno, and queue. For the first time all of these are
fully supported in the Python wrappers. Please see the documents in
the docs directory of the source distribution or at the website for
more details on the types and methods provided.

%description -l pl.UTF-8
Ten moduł dostarcza prawie całkowite opakowanie API C Oracle do
obiektów środowiska baz danych, baz danych, kursorów i transakcji, z
których każdy jest udostępniony jako pythonowy typ w module bsddb3.db.
Obiekty bazy danych mogą używać różnych metod dostępu: btree, hash,
recno i queue. Jest to pierwsza implementacja obsługi tych obiektów
dla Pythona. Więcej szczegółów o typach i metodach znajduje się w
załączonej dokumentacji lub na stronie WWW.

%prep
%setup -q -n %{pname}-%{version}

%build
env CFLAGS="%{rpmcflags}" python3.0 setup.py \
	--berkeley-db-libdir=%{_libdir} \
	--berkeley-db=%{_prefix} \
	build

%install
rm -rf $RPM_BUILD_ROOT
python3.0 -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

# shutup check-files
%py3_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt docs
%dir %{py3_sitedir}/bsddb3
%dir %{py3_sitedir}/bsddb3/tests
%{py3_sitedir}/*.egg-info
%{py3_sitedir}/bsddb3/*.py[co]
%{py3_sitedir}/bsddb3/tests/*.py[co]
%attr(755,root,root) %{py3_sitedir}/bsddb3/*.so

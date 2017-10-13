# Writing up
Writing up for problem with comparison operator '==' vulnerability.

## Problem
Problem is implemented in PHP.
```php
<?php
	$md5 = 'some_user_input';
	if($md5 == md5($md5)){
		echo 'nice';
	}else{
		echo 'whoops';
	}
?>
```

## One of answer
`0e46498610456030`

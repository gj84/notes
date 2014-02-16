// Add this to your theme's functions.php file, and replace wp_link_pages in the whole theme by it.
//Use 
//post intro
//<!--nextpage--><!--pagetitle: Title one -->
//more post
//<!--nextpage--><!--pagetitle: Title two -->
//.....
//That way we get pagination links ... First Title one Title two
//http://wordpress.stackexchange.com/questions/11578/custom-page-links-for-paginated-posts-wp-link-pages-nextpage-quicktag

function wp_link_pages_titled($args = '') {
    $defaults = array(
        'before' => '<p>' . __('Pages:'), 
        'after' => '</p>',
        'link_before' => '', 
        'link_after' => '',
        'echo' => 1
    );

    $r = wp_parse_args( $args, $defaults );
    extract( $r, EXTR_SKIP );

    global $page, $numpages, $multipage, $more, $pagenow, $pages;

    $output = '';
    if ( $multipage ) {
        $output .= $before;
        for ( $i = 1; $i < ($numpages+1); $i = $i + 1 ) {
            $part_content = $pages[$i-1];
            $has_part_title = strpos( $part_content, '<!--pagetitle:' );
            if( 0 === $has_part_title ) {
                $end = strpos( $part_content, '-->' );
                $title = trim( str_replace( '<!--pagetitle:', '', substr( $part_content, 0, $end ) ) );
            }
            $output .= ' ';
            if ( ($i != $page) || ((!$more) && ($page==1)) ) {
                $output .= _wp_link_page($i);
            }
            $title = isset( $title ) && ( strlen( $title ) > 0 ) ? $title : 'First';
            $output .= $link_before . $title . $link_after;
            if ( ($i != $page) || ((!$more) && ($page==1)) )
                $output .= '</a>';
        }
        $output .= $after;
    }
    if ( $echo )
        echo $output;
    return $output;
}